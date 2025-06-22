from flask import Blueprint, jsonify, request, current_app, render_template, redirect, url_for
from .db import get_db_connection

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, task, due_date, reminder, completed FROM todos')
    rows = cur.fetchall()
    todos = [
        {
            'id': row[0],
            'task': row[1],
            'due_date': row[2],
            'reminder': row[3],
            'completed': row[4]
        }
        for row in rows
    ]
    conn.close()
    return render_template('index.html', todos=todos)


@todo_bp.route('/todos', methods=['GET'])
def get_todos():
    conn = current_app.config['GET_DB_CONNECTION']()
    cur = conn.cursor()
    cur.execute('SELECT id, task, due_date, reminder, completed FROM todos')
    rows = cur.fetchall()
    todos = [
        {
            'id': row[0],
            'task': row[1],
            'due_date': row[2],
            'reminder': row[3],
            'completed': row[4]
        }
        for row in rows
    ]
    conn.close()
    return jsonify(todos)


@todo_bp.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    task = data.get('task')
    due_date = data.get('due_date')
    reminder = data.get('reminder', False)

    if not task:
        return jsonify({'error': 'Task is required'}), 400

    conn = current_app.config['GET_DB_CONNECTION']()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO todos (task, due_date, reminder) VALUES (%s, %s, %s) RETURNING id',
        (task, due_date, reminder)
    )
    new_id = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return jsonify({'id': new_id, 'task': task, 'due_date': due_date, 'reminder': reminder}), 201


@todo_bp.route('/add', methods=['POST'])
def add_todo_html():
    task = request.form.get('task')
    due_date = request.form.get('due_date') or None
    reminder = request.form.get('reminder') == 'on'

    if task:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO todos (task, due_date, reminder) VALUES (%s, %s, %s)',
            (task, due_date, reminder)
        )
        conn.commit()
        conn.close()
    return redirect(url_for('todo.index'))


@todo_bp.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM todos WHERE id = %s', (todo_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('todo.index'))


@todo_bp.route('/edit/<int:todo_id>', methods=['GET'])
def edit_todo(todo_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, task, due_date, reminder FROM todos WHERE id = %s', (todo_id,))
    row = cur.fetchone()
    conn.close()

    if row is None:
        return 'Task not found', 404

    todo = {
        'id': row[0],
        'task': row[1],
        'due_date': row[2],
        'reminder': row[3]
    }

    return render_template('edit.html', todo=todo)


@todo_bp.route('/update/<int:todo_id>', methods=['POST'])
def update_todo(todo_id):
    new_task = request.form['task']
    new_due_date = request.form.get('due_date') or None
    new_reminder = request.form.get('reminder') == 'on'
    new_completed = request.form.get('completed') == 'on'

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE todos SET task = %s, due_date = %s, reminder = %s, completed = %s WHERE id = %s',
        (new_task, new_due_date, new_reminder, new_completed, todo_id)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('todo.index'))
