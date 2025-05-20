from flask import Blueprint, jsonify, request
from .db import get_db_connection

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/todos', methods=['GET'])
def get_todos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, task FROM todos;')
    todos = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{'id': t[0], 'task': t[1]} for t in todos])