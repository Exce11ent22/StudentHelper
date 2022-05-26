from datetime import datetime

from flask import Blueprint, render_template, url_for, flash, request
from flask_login import login_user, logout_user
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash, generate_password_hash

from app import login_manager, db
from app.models import User

auth = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('user.questions'))
        else:
            flash('Email or password is not correct')
    return render_template('user/login.html')


@auth.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        password_confirm = request.form['password_confirm']
        university = request.form['university']
        year_of_admission = request.form['year_of_admission']

        if password != password_confirm:
            flash("Пароли не совпадают!")
            return redirect(url_for('auth.registration'))

        if int(datetime.now().year) < int(year_of_admission) or int(year_of_admission) < 1900:
            flash("Год поступления вне диапазона")
            return redirect(url_for('auth.registration'))

        try:
            hash_pwd = generate_password_hash(password)
            new_user = User(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            password=hash_pwd,
                            year_of_admission=year_of_admission,
                            university=university)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        except:
            flash('Такой пользователь уже существует!')
            return redirect(url_for('auth.registration'))

    return render_template('user/registration.html')


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))
