from flask import Flask, request, render_template, jsonify
from todo_logic import update_task, task_list

app = Flask(__name__)
@app.route("/update", methods=["PUT"])
def update():
    data = request.json
    index = data["index"]
    task = data["task"]
    result = update_task(task_list, task, index)
    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=True)