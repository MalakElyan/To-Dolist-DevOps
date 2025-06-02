from flask import Flask
from .routes import todo_bp
from .db import get_db_connection


def create_app():
    app = Flask(__name__)

    from .routes import todo_bp
    app.register_blueprint(todo_bp)

    # ربط دالة الاتصال بالتطبيق
    app.config['GET_DB_CONNECTION'] = get_db_connection

    # إنشاء الجدول عند التشغيل
    with app.app_context():
        init_db()

    return app
