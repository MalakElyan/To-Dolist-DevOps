from flask import Blueprint, jsonify, request, current_app
from .db import get_db_connection

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/')
def index():
    return render_template('index.html')
    
@todo_bp.route('/todos', methods=['GET'])
def get_todos():
    conn = current_app.config['GET_DB_CONNECTION']()
    cur = conn.cursor()
    cur.execute('SELECT id, task FROM todos;')
    rows = cur.fetchall()
    conn.close()
    return jsonify([{'id': row['id'], 'task': row['task']} for row in rows])

@todo_bp.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    task = data.get('task')
    if not task:
        return jsonify({'error': 'Task is required'}), 400

    conn = current_app.config['GET_DB_CONNECTION']()
    cur = conn.cursor()
    cur.execute('INSERT INTO todos (task) VALUES (?);', (task,))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return jsonify({'id': new_id, 'task': task}), 201
