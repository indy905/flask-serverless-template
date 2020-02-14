from flask import Flask
from flask_cors import CORS

from application.configs.config import config_by_name
from application.controllers import *


def create_app(config_name):
    app = Flask(__name__)
    # CORS 설정
    CORS(app)
    # 환경변수 설정
    conf = config_by_name[config_name]
    app.config.from_object(conf)
    app.config['JSON_AS_ASCII'] = False
    # 컨트롤러 blueprint 등록
    register_blueprint(app)
    return app


def register_blueprint(app):
    # 컨트롤러 blueprint 등록
    from .controllers import user_controller
    app.register_blueprint(user_controller.user_blueprint)
