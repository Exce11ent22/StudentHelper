import os
from datetime import datetime
from random import randint

from flask import Blueprint, url_for, flash, request, send_file, jsonify
from sqlalchemy import desc
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect, secure_filename

import config
from app import db
from app.models import User, Verification, Question, Answer, UserAndQuestion, UserAndAnswer, Leaderboard

user = Blueprint('user', __name__)

ELEMENTS_PER_PAGE = 10
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


@user.route('/user_questions', methods=['POST'])
def my_questions():
    user_id = request.form['user_id']
    questions = Question.query.filter_by(user_id=user_id).all()
    if not questions:
        message = {'error': 'You have no questions'}
        return jsonify(message)
    questions = [(question.to_dict(), User.query.get(question.user_id).to_dict()) for question in questions]
    return jsonify(questions)


@user.route('/questions/search', methods=['POST'])
def search_questions():
    search = request.form['search']
    search = search.lower()
    questions = Question.query.all()
    by_header = [question for question in questions if search in str(question.header).lower()]
    by_subj_tag = [question for question in questions if search in str(question.subject_tag).lower()]
    by_description = [question for question in questions if search in str(question.description).lower()]
    questions = by_header + by_subj_tag + by_description
    if len(questions) == 0:
        message = {'error': 'Nothing to find'}
        return jsonify(message)
    end = SEARCH_ELEMENTS
    if len(questions) < end:
        end = len(questions)
    questions = questions[:end]
    questions = [(question.to_dict(), User.query.get(question.user_id).to_dict(), None) for question in questions]
    return jsonify(questions)


@user.route('/questions/<int:page>', methods=['GET', 'POST'])
def questions_pagination(page):
    if request.method == 'POST':
        user_id = request.form['user_id']
    else:
        user_id = None
    if page == 0:
        return redirect(url_for('user.questions_pagination', page=1))
    questions = Question.query.order_by(desc(Question.date_time)).all()
    start = (page - 1) * ELEMENTS_PER_PAGE
    end = page * ELEMENTS_PER_PAGE
    questions_len = len(questions)
    if questions_len == 0:
        message = {'error': 'Not questions yet'}
        return jsonify(message)
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
    if user_id is None:
        questions = [(question.to_dict(), User.query.get(question.user_id).to_dict(), None) for question in questions]
    else:
        questions = [
            (
                question.to_dict(),
                User.query.get(question.user_id).to_dict(),
                UserAndQuestion.query.filter_by(user_id=user_id, question_id=question.id).first().to_dict()
            ) for question in questions
        ]
    return jsonify(
        {
            'questions': questions,
            'page': page,
            'has_next': has_next,
            'has_prev': has_prev
        }
    )


@user.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question(question_id):
    if request.method == 'POST':
        user_id = request.form['user_id']
        description = request.form['description']
        file = request.files['file']
        attachment_path = None
        if file:
            if len(file.filename) > 80:
                message = {'error': 'filename is too long'}
                return jsonify(message)
            filename = secure_filename(file.filename)
            filename = unique_hash(10) + '_' + filename
            attachment_path = '/uploads/answers/' + filename
            file.save(os.path.join(config.BASE_DIR + '/uploads/answers', filename))
        try:
            answer = Answer(
                user_id=user_id,
                description=description,
                question_id=question_id,
                attachment_path=attachment_path
            )
            db.session.add(answer)
            db.session.commit()
        except:
            message = {'error': 'Something wrong'}
            return jsonify(message)
    else:
        user_id = None

    question = Question.query.get(question_id)
    if not question:
        message = {'error': 'Not found such question'}
        return jsonify(message)
    user = User.query.get(question.user_id)
    answers = Answer.query.filter_by(question_id=question.id)
    best = Answer.query.order_by(desc(Answer.rate)).filter_by(question_id=question.id).first()
    question_vote = None
    if not best or best.rate <= 0:
        best = None
    else:
        best = best.to_dict(), User.query.get(best.user_id).to_dict()
    if user_id is None:
        answers = [(answer.to_dict(), User.query.get(answer.user_id).to_dict, None) for answer in answers]
    else:
        user_and_question = UserAndQuestion.query.filter_by(user_id=user_id, question_id=question.id).first()
        if user_and_question:
            question_vote = user_and_question.is_vote_up
        answers = [
            (
                answer.to_dict(),
                User.query.get(answer.user_id).to_dict(),
                UserAndAnswer.query.filter_by(answer_id=answer.id, user_id=user_id).first().to_dict()
            ) for answer in answers
        ]
    return jsonify({
        'question': question.to_dict(),
        'question_vote': question_vote,
        'user': user.to_dict(),
        'best': best,
        'answers': answers,
        'is_anonymous': (user_id is None)
    }
    )


@user.route('/question/<int:question_id>/download')
def question_attachment_download(question_id):
    question = Question.query.get(question_id)
    if not question:
        message = {'error': 'No such question'}
        return jsonify(message)
    if not question.attachment_path:
        message = {'error': 'The question without attachment'}
        return jsonify(message)
    path = config.BASE_DIR + question.attachment_path
    try:
        return send_file(path_or_file=path, as_attachment=True)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


@user.route('/answer/<int:answer_id>/download')
def answer_attachment_download(answer_id):
    answer = Answer.query.get(answer_id)
    if not answer:
        message = {'error': 'No such answer'}
        return jsonify(message)
    if not answer.attachment_path:
        message = {'error': 'The answer without attachment'}
        return jsonify(message)
    path = config.BASE_DIR + answer.attachment_path
    try:
        return send_file(path_or_file=path, as_attachment=True)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


@user.route('/question/<int:question_id>/upvote', methods=['POST'])
def question_upvote(question_id):
    user_id = request.form['user_id']
    question = Question.query.get(question_id)
    if not question:
        flash('Такого вопроса нет')
        return redirect(url_for('user.questions'))
    user_and_question = UserAndQuestion.query.filter_by(user_id=user_id, question_id=question_id).first()
    if user_and_question:
        flash('Уже оценен')
        return redirect(url_for('user.question', question_id=question_id))
    user_and_question = UserAndQuestion(
        user_id=user_id,
        question_id=question_id,
        is_vote_up=True
    )
    question.rate += 1
    user = User.query.get(question.user_id)
    user.rating += 1
    try:
        db.session.add(user_and_question)
        db.session.commit()
        message = {'message': 'Success'}
        return jsonify(message)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


@user.route('/question/<int:question_id>/downvote', methods=['POST'])
def question_downvote(question_id):
    user_id = request.form['user_id']
    question = Question.query.get(question_id)
    if not question:
        flash('Такого вопроса нет')
        return redirect(url_for('user.questions'))
    user_and_question = UserAndQuestion.query.filter_by(user_id=user_id, question_id=question_id).first()
    if user_and_question:
        flash('Уже оценен')
        return redirect(url_for('user.question', question_id=question_id))
    user_and_question = UserAndQuestion(
        user_id=user_id,
        question_id=question_id,
        is_vote_up=False
    )
    question.rate -= 1
    user = User.query.get(question.user_id)
    user.rating -= 1
    try:
        db.session.add(user_and_question)
        db.session.commit()
        message = {'message': 'Success'}
        return jsonify(message)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


@user.route('/answer/<int:answer_id>/upvote', methods=['POST'])
def answer_upvote(answer_id):
    user_id = request.form['user_id']
    answer = Answer.query.get(answer_id)
    if not answer:
        message = {'error': 'No such answer'}
        return jsonify(message)
    user_and_answer = UserAndAnswer.query.filter_by(user_id=user_id, answer_id=answer_id).first()
    if user_and_answer:
        message = {'error': 'Already rated'}
        return jsonify(message)
    user_and_answer = UserAndAnswer(
        user_id=user_id,
        answer_id=answer_id,
        is_vote_up=True
    )
    answer.rate += 1
    user = User.query.get(answer.user_id)
    user.rating += 1
    try:
        db.session.add(user_and_answer)
        db.session.commit()
        message = {'message': 'Success'}
        return jsonify(message)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


@user.route('/answer/<int:answer_id>/downvote', methods=['POST'])
def answer_downvote(answer_id):
    user_id = request.form['user_id']
    answer = Answer.query.get(answer_id)
    if not answer:
        message = {'error': 'No such answer'}
        return jsonify(message)
    user_and_answer = UserAndAnswer.query.filter_by(user_id=user_id, answer_id=answer_id).first()
    if user_and_answer:
        message = {'error': 'Already rated'}
        return jsonify(message)
    user_and_answer = UserAndAnswer(
        user_id=user_id,
        answer_id=answer_id,
        is_vote_up=False
    )
    answer.rate -= 1
    user = User.query.get(answer.user_id)
    user.rating -= 1
    try:
        db.session.add(user_and_answer)
        db.session.commit()
        message = {'message': 'Success'}
        return jsonify(message)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


@user.route('/ask', methods=['POST'])
def ask():
    user_id = request.form['user_id']
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
            user_id=user_id,
            header=header,
            description=description,
            subject_tag=subj_tag,
            attachment_path=attachment_path
        )
        db.session.add(question)
        db.session.commit()
        message = {'message': 'Success'}
        return jsonify(message)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


@user.route('/profile', methods=['POST'])
def profile():
    user_id = request.form['user_id']
    user = User.query.get(user_id)
    return jsonify(
        {
            'user': user.to_dict(),
            'current_id': user_id
        }
    )


@user.route('/profile/<int:user_id>', methods=['POST'])
def profile_by_id(user_id):
    current_user_id = request.form['user_id']
    if user_id == current_user_id:
        return redirect(url_for('user.profile'))
    user = User.query.get(user_id)
    if not user:
        message = {'error': 'No such user'}
        return jsonify(message)
    return jsonify(
        {
            'user': user.to_dict(),
            'current_id': current_user_id
        }
    )


@user.route('/change', methods=['POST'])
def change():
    user = User.query.get(request.form['user_id'])
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    university = request.form['university']
    year_of_admission = request.form['year_of_admission']

    if user.email != email and User.query.filter_by(email=email).first():
        message = {'error': 'The email already existed'}
        return jsonify(message)

    if not check_password_hash(user.password, password):
        message = {'error': 'Wrong password'}
        return jsonify(message)

    if int(datetime.now().year) < int(year_of_admission) or int(year_of_admission) < 1900:
        message = {'error': 'Incorrect year of admission'}
        return jsonify(message)

    try:
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.university = university
        user.year_of_admission = year_of_admission
        db.session.commit()
        message = {'message': 'Success'}
        return jsonify(message)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


@user.route('/verification', methods=['POST'])
def verification():
    user_id = request.form['user_id']
    verif = Verification.query.filter_by(user_id=user_id).first()
    if verif:
        message = {'error': 'Waiting for decision'}
        return jsonify(message)
    speciality = request.form['speciality']
    file = request.files['file']
    if not ('.' in file.filename and file.filename.lower().rsplit('.')[1] in {'jpg', 'png'} and len(
            file.filename) < 80):
        flash('Неправильное расширение файла')
        return redirect(url_for('user.verification'))
    filename = secure_filename(file.filename)
    filename = unique_hash(10) + '_' + filename
    attachment_path = '/uploads/verifications/' + filename
    file.save(os.path.join(config.BASE_DIR + '/uploads/verifications', filename))
    try:
        new_verification = Verification(
            user_id=user_id,
            attachment_path=attachment_path
        )
        db.session.add(new_verification)
        user = User.query.get(user_id)
        user.speciality = speciality
        db.session.commit()
        message = {'message': 'Success'}
        return jsonify(message)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


@user.route('/leaderboard')
def leaderboard():
    leaderboard = Leaderboard.query.order_by(desc(Leaderboard.rating_increase)).limit(10).all()
    leaderboard = [(card.to_dict(), User.query.get(card.user_id).to_dict()) for card in leaderboard]
    return jsonify(leaderboard)
