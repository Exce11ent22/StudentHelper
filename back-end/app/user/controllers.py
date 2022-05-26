import os
from datetime import datetime
from random import randint

from flask import Blueprint, render_template, url_for, flash, request, send_from_directory, send_file
from flask_login import login_user, login_required, current_user
from werkzeug.utils import redirect, secure_filename
from werkzeug.security import check_password_hash, generate_password_hash

import config
from app import login_manager, db
from app.models import User, Verification, Question, Answer

user = Blueprint('user', __name__)


def unique_hash(n):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    nums = '12345678910'
    symbols = '-_'
    chars = lower + upper + nums + symbols
    return ''.join([chars[randint(0, len(chars) - 1)] for x in range(n)])


@user.route('/questions', methods=['POST', 'GET'])
def questions():
    return render_template('user/questions.html')


@user.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question(question_id):
    question = Question.query.get(question_id)
    if not question:
        flash('Такого вопроса нет!')
        return redirect(url_for('user.questions'))
    user = User.query.get(question.user_id)
    answers = Answer.query.filter_by(question_id=question.id)
    return render_template(
        'user/question.html',
        question=question,
        user=user,
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
    return send_file(path_or_file=path, as_attachment=True)


@user.route('/ask', methods=['GET', 'POST'])
@login_required
def ask():
    if request.method == 'POST':
        header = request.form['header']
        description = request.form['description']
        file = request.files['file']
        subj_tag = request.form['subj_tag']
        attachment_path = None
        print(len(file.filename))
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
        pass  # todo
    return render_template('user/verification.html')


@user.route('/leaderboard')
def leaderboard():
    return render_template('user/leaderboard.html')
