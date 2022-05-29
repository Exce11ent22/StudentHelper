import os
from datetime import datetime
from random import randint

from flask import Blueprint, render_template, url_for, flash, request, send_file
from flask_login import login_required, current_user
from sqlalchemy import desc
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect, secure_filename

import config
from app import db
from app.models import User, Verification, Question, Answer, UserAndQuestion, UserAndAnswer, Leaderboard

user = Blueprint('user', __name__)

ELEMENTS_PER_PAGE = 3
SEARCH_ELEMENTS = 50


def unique_hash(n):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    nums = '12345678910'
    symbols = '-_'
    chars = lower + upper + nums + symbols
    return ''.join([chars[randint(0, len(chars) - 1)] for x in range(n)])


@user.route('/questions')
def questions():
    return redirect(url_for('user.questions_pagination', page=1))


@user.route('/my_questions')
@login_required
def my_questions():
    questions = Question.query.filter_by(user_id=current_user.id).all()
    if not questions:
        flash('У вас нет собственных вопросов')
        return redirect(url_for('user.profile'))
    questions = [(question, User.query.get(question.user_id)) for question in questions]
    return render_template(
        'user/questions.html',
        questions=questions,
        page=1,
        has_next=False,
        has_prev=False
    )


@user.route('/questions/search', methods=['POST'])
def search_questions():
    if request.method == 'POST':
        search = request.form['search']
        search = search.lower()
        questions = Question.query.all()
        by_header = [question for question in questions if search in str(question.header).lower()]
        by_subj_tag = [question for question in questions if search in str(question.subject_tag).lower()]
        by_description = [question for question in questions if search in str(question.description).lower()]
        questions = by_header + by_subj_tag + by_description
        if len(questions) == 0:
            flash('Ничего не найдено')
            return redirect(url_for('user.questions'))
        end = SEARCH_ELEMENTS
        if len(questions) < end:
            end = len(questions)
        questions = questions[:end]
        questions = [(question, User.query.get(question.user_id), None) for question in questions]
        return render_template(
            'user/questions.html',
            questions=questions,
            page=1,
            has_next=False,
            has_prev=False
        )
    else:
        return redirect(url_for('user.questions'))


@user.route('/questions/<int:page>', methods=['GET'])
def questions_pagination(page):
    if page == 0:
        return redirect(url_for('user.questions_pagination', page=1))
    questions = Question.query.all()
    start = (page - 1) * ELEMENTS_PER_PAGE
    end = page * ELEMENTS_PER_PAGE
    questions_len = len(questions)
    if questions_len == 0:
        flash('Задайте вопрос первым!')
        return redirect(url_for('user.ask'))
    has_next, has_prev = True, True
    if page == 1:
        has_prev = False
    if start >= questions_len:
        return redirect(url_for('user.questions_pagination', page=1))
    if end > questions_len:
        end = questions_len
        has_next = False
    if start < questions_len <= end:
        has_next = False
        end = questions_len
    questions = questions[start:end]
    if current_user.is_anonymous:
        questions = [(question, User.query.get(question.user_id), None) for question in questions]
    else:
        questions = [
            (
                question,
                User.query.get(question.user_id),
                UserAndQuestion.query.filter_by(user_id=current_user.id, question_id=question.id).first()
            ) for question in questions
        ]
    return render_template(
        'user/questions.html',
        questions=questions,
        page=page,
        has_next=has_next,
        has_prev=has_prev
    )


@user.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question(question_id):
    if request.method == 'POST':
        description = request.form['description']
        file = request.files['file']
        attachment_path = None
        if file:
            if len(file.filename) > 80:
                flash('Слишком длинное название файла')
                return redirect(request.url)
            filename = secure_filename(file.filename)
            filename = unique_hash(10) + '_' + filename
            attachment_path = '/uploads/answers/' + filename
            file.save(os.path.join(config.BASE_DIR + '/uploads/answers', filename))
        try:
            answer = Answer(
                user_id=current_user.id,
                description=description,
                question_id=question_id,
                attachment_path=attachment_path
            )
            db.session.add(answer)
            db.session.commit()
        except:
            flash('Что-то пошло не так')
            return redirect(request.url)

    question = Question.query.get(question_id)
    if not question:
        flash('Такого вопроса нет!')
        return redirect(url_for('user.questions'))
    user = User.query.get(question.user_id)
    answers = Answer.query.filter_by(question_id=question.id)
    best = Answer.query.order_by(desc(Answer.rate)).filter_by(question_id=question.id).first()
    question_vote = None
    if not best or best.rate <= 0:
        best = None
    else:
        best = best, User.query.get(best.user_id)
    if current_user.is_anonymous:
        answers = [(answer, User.query.get(answer.user_id), None) for answer in answers]
    else:
        user_and_question = UserAndQuestion.query.filter_by(user_id=current_user.id, question_id=question.id).first()
        if user_and_question:
            question_vote = user_and_question.is_vote_up
        answers = [
            (
                answer,
                User.query.get(answer.user_id),
                UserAndAnswer.query.filter_by(answer_id=answer.id, user_id=current_user.id).first()
            ) for answer in answers
        ]
    return render_template(
        'user/question.html',
        question=question,
        question_vote=question_vote,
        user=user,
        best=best,
        answers=answers,
        is_anonymous=current_user.is_anonymous)


@user.route('/question/<int:question_id>/download')
def question_attachment_download(question_id):
    question = Question.query.get(question_id)
    if not question:
        flash('Такого вопроса нет!')
        return redirect(url_for('user.questions'))
    if not question.attachment_path:
        flash('Этот вопрос не имеет вложений')
        return redirect(url_for('user.question', question_id=question_id))
    path = config.BASE_DIR + question.attachment_path
    try:
        return send_file(path_or_file=path, as_attachment=True)
    except:
        flash('Такого файла не найдено!')
        return redirect(url_for('user.question', question_id=question_id))


@user.route('/answer/<int:answer_id>/download')
def answer_attachment_download(answer_id):
    answer = Answer.query.get(answer_id)
    if not answer:
        flash('Такого ответа нет!')
        return redirect(url_for('user.questions'))
    if not answer.attachment_path:
        flash('Этот ответ не имеет вложений')
        return redirect(url_for('user.question', question_id=answer.question_id))
    path = config.BASE_DIR + answer.attachment_path
    try:
        return send_file(path_or_file=path, as_attachment=True)
    except:
        flash('Такого файла не найдено!')
        return redirect(url_for('user.question', question_id=answer.question_id))


@user.route('/question/<int:question_id>/upvote')
@login_required
def question_upvote(question_id):
    question = Question.query.get(question_id)
    if not question:
        flash('Такого вопроса нет')
        return redirect(url_for('user.questions'))
    user_and_question = UserAndQuestion.query.filter_by(user_id=current_user.id, question_id=question_id).first()
    if user_and_question:
        flash('Уже оценен')
        return redirect(url_for('user.question', question_id=question_id))
    user_and_question = UserAndQuestion(
        user_id=current_user.id,
        question_id=question_id,
        is_vote_up=True
    )
    question.rate += 1
    user = User.query.get(question.user_id)
    user.rating += 1
    try:
        db.session.add(user_and_question)
        db.session.commit()
        return redirect(url_for('user.question', question_id=question_id))
    except:
        flash('Что-то пошло не так')
        return redirect(url_for('user.question', question_id=question_id))


@user.route('/question/<int:question_id>/downvote')
@login_required
def question_downvote(question_id):
    question = Question.query.get(question_id)
    if not question:
        flash('Такого вопроса нет')
        return redirect(url_for('user.questions'))
    user_and_question = UserAndQuestion.query.filter_by(user_id=current_user.id, question_id=question_id).first()
    if user_and_question:
        flash('Уже оценен')
        return redirect(url_for('user.question', question_id=question_id))
    user_and_question = UserAndQuestion(
        user_id=current_user.id,
        question_id=question_id,
        is_vote_up=False
    )
    question.rate -= 1
    user = User.query.get(question.user_id)
    user.rating -= 1
    try:
        db.session.add(user_and_question)
        db.session.commit()
        return redirect(url_for('user.question', question_id=question_id))
    except:
        flash('Что-то пошло не так')
        return redirect(url_for('user.question', question_id=question_id))


@user.route('/answer/<int:answer_id>/upvote')
@login_required
def answer_upvote(answer_id):
    answer = Answer.query.get(answer_id)
    if not answer:
        flash('Такого ответа нет')
        return redirect(url_for('user.questions'))
    user_and_answer = UserAndAnswer.query.filter_by(user_id=current_user.id, answer_id=answer_id).first()
    if user_and_answer:
        flash('Уже оценен')
        return redirect(url_for('user.question', question_id=answer.question_id))
    user_and_answer = UserAndAnswer(
        user_id=current_user.id,
        answer_id=answer_id,
        is_vote_up=True
    )
    answer.rate += 1
    user = User.query.get(answer.user_id)
    user.rating += 1
    try:
        db.session.add(user_and_answer)
        db.session.commit()
        return redirect(url_for('user.question', question_id=answer.question_id))
    except:
        flash('Что-то пошло не так')
        return redirect(url_for('user.question', question_id=answer.question_id))


@user.route('/answer/<int:answer_id>/downvote')
@login_required
def answer_downvote(answer_id):
    answer = Answer.query.get(answer_id)
    if not answer:
        flash('Такого ответа нет')
        return redirect(url_for('user.questions'))
    user_and_answer = UserAndAnswer.query.filter_by(user_id=current_user.id, answer_id=answer_id).first()
    if user_and_answer:
        flash('Уже оценен')
        return redirect(url_for('user.question', question_id=answer.question_id))
    user_and_answer = UserAndAnswer(
        user_id=current_user.id,
        answer_id=answer_id,
        is_vote_up=False
    )
    answer.rate -= 1
    user = User.query.get(answer.user_id)
    user.rating -= 1
    try:
        db.session.add(user_and_answer)
        db.session.commit()
        return redirect(url_for('user.question', question_id=answer.question_id))
    except:
        flash('Что-то пошло не так')
        return redirect(url_for('user.question', question_id=answer.question_id))


@user.route('/ask', methods=['GET', 'POST'])
@login_required
def ask():
    if request.method == 'POST':
        header = request.form['header']
        description = request.form['description']
        file = request.files['file']
        subj_tag = request.form['subj_tag']
        attachment_path = None
        if file:
            if len(file.filename) > 80:
                flash('Слишком длинное название файла')
                return redirect(request.url)
            filename = secure_filename(file.filename)
            filename = unique_hash(10) + '_' + filename
            attachment_path = '/uploads/questions/' + filename
            file.save(os.path.join(config.BASE_DIR + '/uploads/questions', filename))

        try:
            question = Question(
                user_id=current_user.id,
                header=header,
                description=description,
                subject_tag=subj_tag,
                attachment_path=attachment_path
            )
            db.session.add(question)
            db.session.commit()
            return redirect(url_for('user.questions'))
        except:
            flash('Что-то пошло не так')
            return redirect(request.url)

    return render_template('user/ask.html')


@user.route('/profile')
@login_required
def profile():
    user = User.query.get(current_user.id)
    return render_template('user/profile.html', user=user, current_id=current_user.id)


@user.route('/profile/<int:user_id>')
@login_required
def profile_by_id(user_id):
    if user_id == current_user.id:
        return redirect(url_for('user.profile'))
    user = User.query.get(user_id)
    if not user:
        flash('Такого пользователя не существует!')
        return redirect(url_for('user.profile'))
    return render_template('user/profile.html', user=user, current_id=current_user.id)


@user.route('/change', methods=['GET', 'POST'])
@login_required
def change():
    user = User.query.get(current_user.id)
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        university = request.form['university']
        year_of_admission = request.form['year_of_admission']

        if current_user.email != email and User.query.filter_by(email=email).first():
            flash('Такая почта уже существует')
            return redirect(url_for('user.change'))

        if not check_password_hash(current_user.password, password):
            flash('Неверный пароль!')
            return redirect(url_for('user.change'))

        if int(datetime.now().year) < int(year_of_admission) or int(year_of_admission) < 1900:
            flash("Укажите верный год поступления")
            return redirect(url_for('user.change'))

        try:
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.university = university
            user.year_of_admission = year_of_admission
            db.session.commit()
            return redirect(url_for('user.profile'))
        except:
            flash('Что-то пошло не так')
            return redirect(url_for('user.change'))

    return render_template('user/change.html', user=user)


@user.route('/verification', methods=['GET', 'POST'])
@login_required
def verification():
    verif = Verification.query.filter_by(user_id=current_user.id).first()
    if verif:
        flash('Ожидается подтверждение')
        return redirect(url_for('user.profile'))
    if request.method == 'POST':
        speciality = request.form['speciality']
        file = request.files['file']
        if not ('.' in file.filename and file.filename.lower().rsplit('.')[1] in {'jpg', 'png'} and len(file.filename) < 80):
            flash('Неправильное расширение файла')
            return redirect(url_for('user.verification'))
        filename = secure_filename(file.filename)
        filename = unique_hash(10) + '_' + filename
        attachment_path = '/uploads/verifications/' + filename
        file.save(os.path.join(config.BASE_DIR + '/uploads/verifications', filename))
        try:
            new_verification = Verification(
                user_id=current_user.id,
                attachment_path=attachment_path
            )
            db.session.add(new_verification)
            user = User.query.get(current_user.id)
            user.speciality = speciality
            db.session.commit()
            return redirect(url_for('user.profile'))
        except:
            flash('Что-то пошло не так')
            return redirect(url_for('user.verification'))

    return render_template('user/verification.html')


@user.route('/leaderboard')
def leaderboard():
    leaderboard = Leaderboard.query.order_by(desc(Leaderboard.rating_increase)).limit(10).all()
    leaderboard = [(card, User.query.get(card.user_id)) for card in leaderboard]
    return render_template('user/leaderboard.html', leaderboard=leaderboard)
