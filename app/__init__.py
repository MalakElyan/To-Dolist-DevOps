from flask import Flask
from .routes import todo_bp
from .db import get_db_connection, init_db  # ✅ استيراد الدوال

def create_app():
    app = Flask(__name__)
    app.register_blueprint(todo_bp)
    app.config['GET_DB_CONNECTION'] = get_db_connection # ربط دالة اللاتصال بالتطبيق
    init_db()  # ✅ تهيئة قاعدة البيانات
    return app
