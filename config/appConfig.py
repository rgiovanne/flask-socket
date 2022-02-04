import datetime
from flask import Flask
from flask_cors import CORS
from config.environment import JWT_SECRET_KEY

def create_app():

    app = Flask(__name__)
    CORS(app, support_credentials=True)
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['SECRET_KEY'] = 'secret!'
    app.config['Access-Control-Allow-Origin'] = '*'
    app.config['SESSION_TYPE'] = 'filesystem'

    return app
