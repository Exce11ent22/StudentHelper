from typing import Any

from flask import Flask, jsonify
from flask import json
from flask_sqlalchemy import SQLAlchemy
from safrs import SAFRSAPI


class ModelEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if hasattr(o, 'to_json'):
            return o.to_json()
        else:
            return super(ModelEncoder, self).default(o)


app = Flask(__name__)
app.config.from_object('config')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.json_encoder = ModelEncoder

swagger = SAFRSAPI(app=app, prefix='/apidocs')

db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    message = {'error': '404'}
    return jsonify(message)


@app.errorhandler(413)
def not_found(error):
    message = {'error': '413'}
    return jsonify(message)


@app.route('/<int:c>')
def index_with_param(c):
    return str(c)


from app.authorisation.controllers import auth
from app.user.controllers import user
from app.admin.controllers import admin

app.register_blueprint(auth)
app.register_blueprint(user)
app.register_blueprint(admin)


db.create_all()
