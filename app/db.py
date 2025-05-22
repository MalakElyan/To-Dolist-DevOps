import sqlite3
import os

# تحديد مسار ملف قاعدة البيانات
DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'todo.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # حتى يرجع الصفوف كقواميس بدلاً من tuples
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
