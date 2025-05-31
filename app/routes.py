from flask import Blueprint, jsonify, request, current_app, render_template, redirect, url_for
from .db import get_db_connection

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, task FROM todos')
    todos = cur.fetchall()
    conn.close()
    return render_template('index.html', todos=todos)

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

@todo_bp.route('/add', methods=['POST'])
def add_todo_html():
    task = request.form.get('task')
    if task:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO todos (task) VALUES (?);', (task,))
        conn.commit()
        conn.close()
    return redirect(url_for('todo.index'))

@todo_bp.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('todo.index'))
