import os

from flask import Blueprint, url_for, flash, request, send_file, jsonify
from werkzeug.utils import redirect

import config
from app import db
from app.models import User, Verification, Question, Answer, Leaderboard, LeaderboardTimestamp

admin = Blueprint('admin', __name__)

ELEMENTS_PER_PAGE = 3
SEARCH_ELEMENTS = 50


@admin.route('/admin_questions', methods=['POST'])
def questions():
    user = User.query.get(request.form['user_id'])
    if not user.is_administrator or not user.is_moderator:
        message = {'error': 'Access denied'}
        return jsonify(message)
    return redirect(url_for('admin.questions_pagination', page=1))


@admin.route('/admin_questions/search', methods=['POST'])
def search_questions():
    user = User.query.get(request.form['user_id'])
    if not user.is_administrator or not user.is_moderator:
        message = {'error': 'Access denied'}
        return jsonify(message)
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
    questions = [(question.to_dict(), User.query.get(question.user_id).to_dict()) for question in questions]
    return jsonify(questions)


@admin.route('/admin_questions/<int:page>', methods=['POST'])
def questions_pagination(page):
    user = User.query.get(request.form['user_id'])
    if not user.is_administrator or not user.is_moderator:
        message = {'error': 'Access denied'}
        return jsonify(message)
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
    questions = [(question.to_dict(), User.query.get(question.user_id).to_dict()) for question in questions]
    return jsonify(questions)


@admin.route('/admin_question/<int:question_id>', methods=['POST'])
def question(question_id):
    user = User.query.get(request.form['user_id'])
    if not user.is_administrator or not user.is_moderator:
        message = {'error': 'Access denied'}
        return jsonify(message)
    question = Question.query.get(question_id)
    if not question:
        flash('Такого вопроса нет!')
        return redirect(url_for('admin.questions'))
    user = User.query.get(question.user_id)
    answers = Answer.query.filter_by(question_id=question.id)
    answers = [(answer.to_dict(), User.query.get(answer.user_id).to_dict()) for answer in answers]
    return jsonify(question.to_dict(), user.to_dict(), answers)


@admin.route('/admin_question/delete/<int:question_id>', methods=['POST'])
def question_delete(question_id):
    user = User.query.get(request.form['user_id'])
    if not user.is_administrator or not user.is_moderator:
        message = {'error': 'Access denied'}
        return jsonify(message)
    try:
        question = Question.query.get(question_id)
        if question.attachment_path:
            path = os.path.join(config.BASE_DIR, question.attachment_path[1:])
            os.remove(path)
        db.session.delete(question)
        db.session.commit()
        message = {'message': 'Success'}
        return jsonify(message)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


@admin.route('/admin_answer/delete/<int:answer_id>', methods=['POST'])
def answer_delete(answer_id):
    user = User.query.get(request.form['user_id'])
    if not user.is_administrator or not user.is_moderator:
        message = {'error': 'Access denied'}
        return jsonify(message)
    try:
        answer = Answer.query.get(answer_id)
        print('нашел ответ')
        question_id = answer.question_id
        if answer.attachment_path:
            path = os.path.join(config.BASE_DIR, answer.attachment_path[1:])
            os.remove(path)
        db.session.delete(answer)
        db.session.commit()
        message = {'message': 'Success'}
        return jsonify(message)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


@admin.route('/list_of_administrators', methods=['POST'])
def list_of_admins():
    user = User.query.get(request.form['user_id'])
    if not user.is_administrator:
        message = {'error': 'Access denied'}
        return jsonify(message)
    admins = User.query.filter_by(role=User.ADMINISTRATOR).all()
    moders = User.query.filter_by(role=User.MODERATOR).all()
    return jsonify([admin.to_dict() for admin in admins], [moder.to_dict() for moder in moders])


@admin.route('/admin_verifications', methods=['POST'])
def verifications():
    user = User.query.get(request.form['user_id'])
    if not user.is_administrator:
        message = {'error': 'Access denied'}
        return jsonify(message)
    verifs = Verification.query.all()
    verifs = [(verif.to_dict(), User.query.get(verif.user_id).to_dict()) for verif in verifs]
    return jsonify(verifs)


@admin.route('/admin_verification/<int:verif_id>', methods=['POST'])
def verification(verif_id):
    user = User.query.get(request.form['user_id'])
    if not user.is_administrator:
        message = {'error': 'Access denied'}
        return jsonify(message)
    verif = Verification.query.get(verif_id)
    if not verif:
        message = {'error': 'No such verification order'}
        return jsonify(message)
    user = User.query.get(verif.user_id)
    return jsonify(verif.to_dict(), user.to_dict())


@admin.route('/admin_verification/<int:verif_id>/download', methods=['POST'])
def verification_download(verif_id):
    user = User.query.get(request.form['user_id'])
    if not user.is_administrator:
        message = {'error': 'Access denied'}
        return jsonify(message)
    verif = Verification.query.get(verif_id)
    if not verif:
        message = {'error': 'No such verification order'}
        return jsonify(message)

    path = config.BASE_DIR + verif.attachment_path
    try:
        return send_file(path_or_file=path, as_attachment=True)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


@admin.route('/accept_verification/<int:verif_id>', methods=['POST'])
def accept_verification(verif_id):
    user = User.query.get(request.form['user_id'])
    if not user.is_administrator:
        message = {'error': 'Access denied'}
        return jsonify(message)
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
        message = {'message': 'Success'}
        return jsonify(message)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


@admin.route('/delete_verification/<int:verif_id>', methods=['POST'])
def delete_verification(verif_id):
    user = User.query.get(request.form['user_id'])
    if not user.is_administrator:
        message = {'error': 'Access denied'}
        return jsonify(message)
    verif = Verification.query.get(verif_id)
    if not verif:
        message = {'error': 'No such verification order'}
        return jsonify(message)
    try:
        path = os.path.join(config.BASE_DIR, verif.attachment_path[1:])
        os.remove(path)
        db.session.delete(verif)
        db.session.commit()
        message = {'message': 'Success'}
        return jsonify(message)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


@admin.route('/assign_role', methods=['POST'])
def assign_role():
    user = User.query.get(request.form['user_id'])
    if not user.is_administrator:
        message = {'error': 'Access denied'}
        return jsonify(message)
    email = request.form['email']
    role = request.form['role']
    user = User.query.filter_by(email=email).first()
    if not user:
        message = {'error': 'No such user'}
        return jsonify(message)
    if user.role == User.MODERATOR or user.role == User.ADMINISTRATOR:
        message = {'error': 'The user is already has a role'}
        return jsonify(message)
    try:
        user.role = User.MODERATOR if role == 'moderator' else User.ADMINISTRATOR
        db.session.commit()
        message = {'message': 'Success'}
        return jsonify(message)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


@admin.route('/delete_role/<int:user_id>', methods=['POST'])
def delete_role(user_id):
    user = User.query.get(request.form['user_id'])
    if not user.is_administrator:
        message = {'error': 'Access denied'}
        return jsonify(message)
    user = User.query.get(user_id)
    if not user:
        message = {'error': 'No such user'}
        return jsonify(message)
    try:
        user.role = User.USER
        db.session.commit()
        message = {'message': 'Success'}
        return jsonify(message)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


@admin.route('/change_role/<int:user_id>', methods=['POST'])
def change_role(user_id):
    user = User.query.get(request.form['user_id'])
    if not user.is_administrator:
        message = {'error': 'Access denied'}
        return jsonify(message)
    user = User.query.get(user_id)
    if not user:
        message = {'error': 'No such user'}
        return jsonify(message)
    role = request.form['role']
    try:
        user.role = User.MODERATOR if role == 'moderator' else User.ADMINISTRATOR
        print(user.role)
        db.session.commit()
        message = {'message': 'Success'}
        return jsonify(message)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)


def get_views_from_api():
    return 15000


@admin.route('/leaderboard_refresh', methods=['POST'])
def leaderboard_refresh():
    user = User.query.get(request.form['user_id'])
    if not user.is_administrator:
        message = {'error': 'Access denied'}
        return jsonify(message)
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
        message = {'message': 'Success'}
        return jsonify(message)
    except:
        message = {'error': 'Something wrong'}
        return jsonify(message)

