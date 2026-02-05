from flask import Flask, request, jsonify
from todo_logic import update_task, task_list, add_task, delete_task
from database import engine, metadata
import models

app = Flask(__name__)



@app.route("/task/<int:index>", methods=["PUT"])
def update_task_route(index):
    data = request.json
    task = data["task"]
    result = update_task(task_list, task, index)
    return jsonify(result)

@app.route("/task", methods=["GET"])
def get_task_route():
    return jsonify(task_list)

@app.route("/task", methods=["POST"])
def add_task_route():
    data = request.json
    task = data["task"]
    result = add_task(task_list, task)
    return jsonify(result)

@app.route("/task/<int:index>", methods=["DELETE"])
def delete_task_route(index):
    result = delete_task(task_list, index)
    return jsonify(result)

if __name__ == "__main__":
    metadata.create_all(engine)
    app.run(debug=True)