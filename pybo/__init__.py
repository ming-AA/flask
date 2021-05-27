from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__) # Flask 애플리케이션 생성, __name__ 모듈명 (pybo)
    app.config.from_object(config)

    # ORM
    db.init_app(app) # SQLAlchemy 초기화
    migrate.init_app(app, db) # Migrate 초기화
    from . import models # migrate 객체가 models.py 파일 참조

    # 블루프린트
    from .views import main_views, question_views
    app.register_blueprint(main_views.bp) # 블루프린트 객체 bp 등록
    app.register_blueprint(question_views.bp)

    return app