from pymongo import MongoClient
import os

# Настройка MongoDB
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/taskdb"))
db = client.taskdb

# Добавление тестовых данных, если база данных пуста
if "tasks" not in db.list_collection_names():
    db.tasks.insert_many([
        {"title": "Уйти на каникулы", "done": False},
        {"title": "Сдать лабу по докеру", "done": True}
    ])
    print("Database initialized!")
else:
    print("Database already initialized.")