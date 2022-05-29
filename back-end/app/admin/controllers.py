import os

from flask import Blueprint, render_template, url_for, flash, request, send_file
from flask_login import login_required, current_user
from werkzeug.utils import redirect

import config
from app import db
from app.models import User, Verification, Question, Answer, Leaderboard, LeaderboardTimestamp

admin = Blueprint('admin', __name__)

ELEMENTS_PER_PAGE = 3
SEARCH_ELEMENTS = 50


@admin.route('/admin_questions')
@login_required
def questions():
    if not current_user.is_administrator or not current_user.is_moderator:
        flash('Доступ запрещен')
        return redirect(url_for('index'))
    return redirect(url_for('admin.questions_pagination', page=1))


@admin.route('/admin_questions/search', methods=['POST'])
@login_required
def search_questions():
    if not current_user.is_administrator or not current_user.is_moderator:
        flash('Доступ запрещен')
        return redirect(url_for('index'))
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
        questions = [(question, User.query.get(question.user_id)) for question in questions]
        return render_template(
            'admin/admin_questions.html',
            questions=questions,
            page=1,
            has_next=False,
            has_prev=False
        )
    else:
        return redirect(url_for('user.questions'))


@admin.route('/admin_questions/<int:page>', methods=['GET', 'POST'])
@login_required
def questions_pagination(page):
    if not current_user.is_administrator or not current_user.is_moderator:
        flash('Доступ запрещен')
        return redirect(url_for('index'))
    if page == 0:
        return redirect(url_for('admin.questions_pagination', page=1))
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
        return redirect(url_for('admin.questions_pagination', page=1))
    if end > questions_len:
        end = questions_len
        has_next = False
    if start < questions_len <= end:
        has_next = False
        end = questions_len
    questions = questions[start:end]
    questions = [(question, User.query.get(question.user_id)) for question in questions]
    return render_template(
        'admin/admin_questions.html',
        questions=questions,
        page=page,
        has_next=has_next,
        has_prev=has_prev
    )


@admin.route('/admin_question/<int:question_id>', methods=['GET', 'POST'])
@login_required
def question(question_id):
    if not current_user.is_administrator or not current_user.is_moderator:
        flash('Доступ запрещен')
        return redirect(url_for('index'))
    question = Question.query.get(question_id)
    if not question:
        flash('Такого вопроса нет!')
        return redirect(url_for('admin.questions'))
    user = User.query.get(question.user_id)
    answers = Answer.query.filter_by(question_id=question.id)
    answers = [(answer, User.query.get(answer.user_id)) for answer in answers]
    return render_template(
        'admin/admin_question.html',
        question=question,
        user=user,
        answers=answers)


@admin.route('/admin_question/delete/<int:question_id>')
@login_required
def question_delete(question_id):
    if not current_user.is_administrator or not current_user.is_moderator:
        flash('Доступ запрещен')
        return redirect(url_for('index'))
    try:
        question = Question.query.get(question_id)
        if question.attachment_path:
            path = os.path.join(config.BASE_DIR, question.attachment_path[1:])
            os.remove(path)
        db.session.delete(question)
        db.session.commit()
        return redirect(url_for('admin.questions'))
    except:
        flash('Такого вопроса нет!')
        return redirect(url_for('admin.questions'))


@admin.route('/admin_answer/delete/<int:answer_id>')
@login_required
def answer_delete(answer_id):
    if not (current_user.is_administrator() or current_user.is_moderator()):
        flash('Доступ запрещен')
        return redirect(url_for('index'))
    try:
        answer = Answer.query.get(answer_id)
        print('нашел ответ')
        question_id = answer.question_id
        if answer.attachment_path:
            path = os.path.join(config.BASE_DIR, answer.attachment_path[1:])
            os.remove(path)
        db.session.delete(answer)
        db.session.commit()
        return redirect(url_for('admin.question', question_id=question_id))
    except:
        flash('Такого ответа нет!')
        return redirect(url_for('admin.questions'))


@admin.route('/list_of_administrators')
@login_required
def list_of_admins():
    if not current_user.is_administrator():
        flash('Доступ запрещен')
        return redirect(url_for('index'))
    admins = User.query.filter_by(role=User.ADMINISTRATOR).all()
    moders = User.query.filter_by(role=User.MODERATOR).all()
    return render_template(
        'admin/admin_list_of_administrators.html',
        admins=admins,
        moders=moders
    )


@admin.route('/admin_verifications')
@login_required
def verifications():
    if not current_user.is_administrator():
        flash('Доступ запрещен')
        return redirect(url_for('index'))
    verifs = Verification.query.all()
    verifs = [(verif, User.query.get(verif.user_id)) for verif in verifs]
    return render_template('admin/admin_verifications.html', verifs=verifs)


@admin.route('/admin_verification/<int:verif_id>')
@login_required
def verification(verif_id):
    if not current_user.is_administrator():
        flash('Доступ запрещен')
        return redirect(url_for('index'))
    verif = Verification.query.get(verif_id)
    if not verif:
        flash('Такой заявки нет!')
        return redirect(url_for('admin.verifications'))
    user = User.query.get(verif.user_id)
    return render_template('admin/admin_verification.html', verif=verif, user=user)


@admin.route('/admin_verification/<int:verif_id>/download')
@login_required
def verification_download(verif_id):
    if not current_user.is_administrator():
        flash('Доступ запрещен')
        return redirect(url_for('index'))
    verif = Verification.query.get(verif_id)
    if not verif:
        flash('Такой заявки нет нет!')
        return redirect(url_for('user.questions'))

    path = config.BASE_DIR + verif.attachment_path
    try:
        return send_file(path_or_file=path, as_attachment=True)
    except:
        flash('Такого файла не найдено!')
        return redirect(url_for('admin.verifications'))


@admin.route('/accept_verification/<int:verif_id>')
@login_required
def accept_verification(verif_id):
    if not current_user.is_administrator():
        flash('Доступ запрещен')
        return redirect(url_for('index'))
    verif = Verification.query.get(verif_id)
    if not verif:
        flash('Такой заявки нет нет!')
        return redirect(url_for('user.questions'))
    user = User.query.get(verif.user_id)
    try:
        path = os.path.join(config.BASE_DIR, verif.attachment_path[1:])
        os.remove(path)
        user.verified = True
        db.session.delete(verif)
        db.session.commit()
    except:
        flash('Что-то пошло не так')
    return redirect(url_for('admin.verifications'))


@admin.route('/delete_verification/<int:verif_id>')
@login_required
def delete_verification(verif_id):
    if not current_user.is_administrator():
        flash('Доступ запрещен')
        return redirect(url_for('index'))
    verif = Verification.query.get(verif_id)
    if not verif:
        flash('Такой заявки нет нет!')
        return redirect(url_for('user.questions'))
    try:
        path = os.path.join(config.BASE_DIR, verif.attachment_path[1:])
        os.remove(path)
        db.session.delete(verif)
        db.session.commit()
    except:
        flash('Что-то пошло не так')
    return redirect(url_for('admin.verifications'))


@admin.route('/assign_role', methods=['GET', 'POST'])
@login_required
def assign_role():
    if not current_user.is_administrator():
        flash('Доступ запрещен')
        return redirect(url_for('index'))
    if request.method == 'POST':
        email = request.form['email']
        role = request.form['role']
        user = User.query.filter_by(email=email).first()
        if not user:
            flash('Такого пользователя нет')
            return redirect(url_for('admin.assign_role'))
        if user.role == User.MODERATOR or user.role == User.ADMINISTRATOR:
            flash('Пользователь уже имеет управляющую роль')
            return redirect(url_for('admin.assign_role'))
        try:
            user.role = User.MODERATOR if role == 'moderator' else User.ADMINISTRATOR
            db.session.commit()
        except:
            flash('Что-то пошло не так')
            return redirect(url_for('admin.assign_role'))
    return render_template('admin/admin_assign_role.html')


@admin.route('/delete_role/<int:user_id>')
@login_required
def delete_role(user_id):
    if not current_user.is_administrator():
        flash('Доступ запрещен')
        return redirect(url_for('index'))
    user = User.query.get(user_id)
    if not user:
        flash('Такого пользователя нет')
        return redirect(url_for('admin.list_of_admins'))
    try:
        user.role = User.USER
        db.session.commit()
        return redirect(url_for('admin.list_of_admins'))
    except:
        flash('Что-то пошло не так')
        return redirect(url_for('admin.'))


@admin.route('/change_role/<int:user_id>', methods=['GET', 'POST'])
@login_required
def change_role(user_id):
    if not current_user.is_administrator():
        flash('Доступ запрещен')
        return redirect(url_for('index'))
    user = User.query.get(user_id)
    if not user:
        flash('Такого пользователя нет')
        return redirect(url_for('admin.list_of_admins'))
    if request.method == 'POST':
        role = request.form['role']
        try:
            user.role = User.MODERATOR if role == 'moderator' else User.ADMINISTRATOR
            print(user.role)
            db.session.commit()
            return redirect(url_for('admin.list_of_admins'))
        except:
            flash('Что-то пошло не так')
    return render_template('admin/admin_change_role.html')


def get_views_from_api():
    return 15000


@admin.route('/leaderboard_refresh')
@login_required
def leaderboard_refresh():
    if not current_user.is_administrator():
        flash('Доступ запрещен')
        return redirect(url_for('index'))
    try:
        Leaderboard.query.delete()
        users = User.query.all()
        new_leaderboard = []
        for user in users:
            leaderboard_timestamp = LeaderboardTimestamp.query.filter_by(user_id=user.id).first()
            if leaderboard_timestamp:
                increase = user.rating - leaderboard_timestamp.user_rating
            else:
                increase = user.rating
            points = int(round(increase * get_views_from_api() * 0.00576))
            lead_card = Leaderboard(
                user_id=user.id,
                rating_increase=increase,
                points=points
            )
            new_leaderboard.append(lead_card)

        LeaderboardTimestamp.query.delete()
        for nl in new_leaderboard:
            db.session.add(nl)
        for user in users:
            db.session.add(
                LeaderboardTimestamp(
                    user_id=user.id,
                    user_rating=user.rating
                )
            )
        db.session.commit()
        return redirect(url_for('user.leaderboard'))
    except:
        flash('Что-то пошло не так')
        return redirect(url_for('admin.questinos'))

