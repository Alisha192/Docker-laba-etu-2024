from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

# Используем переменные окружения
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/taskdb")
mongo = PyMongo(app)

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Task API!"})

# Получить все задачи
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = mongo.db.tasks.find()
    return jsonify([task for task in tasks])

# Добавить задачу
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    title = data.get("title")
    done = data.get("done", False)
    task_id = mongo.db.tasks.insert_one({"title": title, "done": done}).inserted_id
    return jsonify({"id": str(task_id)}), 201

# Обновить задачу
@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    mongo.db.tasks.update_one({"_id": task_id}, {"$set": data})
    return jsonify({"message": "Task updated successfully"})

# Удалить задачу
@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    mongo.db.tasks.delete_one({"_id": task_id})
    return jsonify({"message": "Task deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)