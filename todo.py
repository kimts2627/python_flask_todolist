from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(): # 애플리케이션 팩토리 : 순환참조 방지
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from app.models import todo

    # 블루프린트
    from app.views import main_view, todo_view
    app.register_blueprint(main_view.bp)
    app.register_blueprint(todo_view.bp)

    return app