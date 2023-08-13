# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    a = request.args["a"]
    b = request.args["b"]
    return str(operations.add(int(a),int(b)))

@app.route('/sub')
def sub():
    a = request.args["a"]
    b = request.args["b"]
    return str(operations.sub(int(a),int(b)))

@app.route('/mult')
def mult():
    a = request.args["a"]
    b = request.args["b"]
    return str(operations.mult(int(a),int(b)))

@app.route('/div')
def div():
    a = request.args["a"]
    b = request.args["b"]
    return str(operations.div(int(a),int(b)))


@app.route('/math/<operation>')
def math(operation):
    a = request.args["a"]
    b = request.args["b"]
    match operation:
        case "add":
            return str(operations.add(int(a),int(b)))
        case "sub":
            return str(operations.sub(int(a),int(b)))
        case "mult":
            return str(operations.mult(int(a),int(b)))
        case "div":
            return str(operations.div(int(a),int(b)))
        case _:
            return "Bad Query"

    return str(operations.div(int(a),int(b)))