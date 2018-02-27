from flask import Flask, request, Response, jsonify, json


app = Flask(__name__)
data = {}


@app.route("/", methods = ['GET'])
def hello():
    return ("Hello World!")


@app.route('/user', methods=['POST'])
def new_users():
    name = request.form["name"]
    return "Hello {}!".format(name)


@app.route('/users', methods = ['POST'])
def new_name():
    content = request.form["name"]
    num = add_dict(content)
    output = { 'Name' : content, 'ID' : num}
    response = jsonify(output)
    response.status_code = 201
    return response


@app.route('/users/<int:index>', methods = ['GET'])
def view_name(index):
    global data
    if index not in data:
        output = {'Error' : "No User", 'ID' : index}
        response = jsonify(output)
        response.status_code = 204
        return response
    elif index in data:
        output = { 'Name' : data[index], 'ID' : index}
        response = jsonify(output)
        response.status_code = 200
        return response


@app.route('/users/<int:index>', methods = ['DELETE'])
def del_name(index):
    global data
    if index not in data:
        return "No Users", 204
    elif index in data:
        response = jsonify("")
        response.status_code = 204
        del data[index]
        return response


def add_dict(x):
    global data
    i = len(data)
    data[i+1] = x
    return (i+1)









