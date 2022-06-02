from datetime import datetime

from flask import Blueprint, url_for, flash, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import redirect

from app import db
from app.models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        return jsonify(user)
    else:
        message = {'error': 'Unable to get such user'}


@auth.route('/registration', methods=['POST'])
def registration():
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
        return jsonify(new_user)
    except Exception as e:
        message = {'error': e}
        return jsonify(message)
