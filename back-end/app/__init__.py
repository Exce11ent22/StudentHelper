from flasgger import Swagger, swag_from
from flask import Flask, render_template, url_for, redirect, flash, request
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from safrs import SAFRSAPI

app = Flask(__name__)
app.config.from_object('config')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
api = SAFRSAPI(app, prefix='/api/v1/swagger')


@login_manager.unauthorized_handler
def unauthorized():
    flash("Нужно войти в аккаунт")
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(413)
def not_found(error):
    flash("Размер файла слишком большой!")
    return redirect(request.url)


@app.route('/<int:c>')
def index_with_param(c):
    return str(c)


@app.route('/')
def index():
    return render_template('index.html', is_anonimous=current_user.is_anonymous)


from app.authorisation.controllers import auth
from app.user.controllers import user
from app.admin.controllers import admin

app.register_blueprint(auth)
app.register_blueprint(user)
app.register_blueprint(admin)



db.create_all()
