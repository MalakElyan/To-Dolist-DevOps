from flask import Flask
import sqlite3
import os

# تحديد مسار قاعدة البيانات
DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'todo.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL
            );
        ''')
        conn.commit()

def create_app():
    app = Flask(__name__)

    from .routes import todo_bp
    app.register_blueprint(todo_bp)

    # إنشاء قاعدة البيانات عند تشغيل التطبيق
    init_db()

    # جعل دالة الاتصال متاحة لباقي الملفات
    app.config['GET_DB_CONNECTION'] = get_db_connection


    return app
