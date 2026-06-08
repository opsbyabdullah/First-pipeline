from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []


@app.route("/")
def home():
    return jsonify({"message": "Task Manager API"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    task = {"id": len(tasks) + 1, "title": data["title"]}

    tasks.append(task)

    return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]

    return jsonify({"message": "Task deleted"})


if __name__ == "__main__":
    app.run(debug=True)
