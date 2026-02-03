from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Backend service URL
BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:5001')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "service": "frontend"})

@app.route('/api/proxy/tasks', methods=['GET'])
def get_tasks():
    try:
        response = requests.get(f'{BACKEND_URL}/api/tasks')
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({"error": "Backend service unavailable"}), 503

@app.route('/api/proxy/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        response = requests.post(f'{BACKEND_URL}/api/tasks', json=data)
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Backend service unavailable"}), 503

@app.route('/api/proxy/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        data = request.get_json()
        response = requests.put(f'{BACKEND_URL}/api/tasks/{task_id}', json=data)
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Backend service unavailable"}), 503

@app.route('/api/proxy/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        response = requests.delete(f'{BACKEND_URL}/api/tasks/{task_id}')
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Backend service unavailable"}), 503

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=True)