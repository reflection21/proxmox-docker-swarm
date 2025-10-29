from flask import Flask, jsonify, request


app = Flask(__name__)

todos = []

@app.route("/api/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/api/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    todos.append({"id": len(todos)+1, "task": data["task"]})
    return jsonify({"success": True, "todos": todos})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
