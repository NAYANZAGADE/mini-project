from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

# In-memory storage for demo purposes
tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False, "created_at": "2024-01-01"},
    {"id": 2, "title": "Build microservices", "completed": True, "created_at": "2024-01-02"}
]

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        "message": "Task Manager Backend API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "tasks": "/api/tasks",
            "create_task": "POST /api/tasks",
            "update_task": "PUT /api/tasks/{id}",
            "delete_task": "DELETE /api/tasks/{id}"
        }
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "backend"})

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    new_task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    data = request.get_json()
    if 'completed' in data:
        task['completed'] = data['completed']
    if 'title' in data:
        task['title'] = data['title']
    
    return jsonify(task)

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({"message": "Task deleted"})

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)