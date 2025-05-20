from flask import Blueprint, jsonify, request

todo_bp = Blueprint('todo', __name__)

todos = []

@todo_bp.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@todo_bp.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    todos.append(data)
    return jsonify({'message': 'Todo added!'}), 201
