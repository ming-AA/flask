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
    db.init_app(app)
    migrate.init_app(app, db)

    # 블루프린트
    from .views import main_views
    app.register_blueprint(main_views.bp) # 블루프린트 객체 bp 등록

    return app