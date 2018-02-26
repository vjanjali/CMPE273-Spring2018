from flask import Flask, request


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
    add_dict(content)
    return "POST User {}".format(data), 201


@app.route('/users/<int:index>', methods = ['GET'])
def view_name(index):
    if index not in data:
        return "No Users", 204
    elif index in data:
        output = '{' + str(index) + ':' + data[index] + '}'
        return "GET User {}".format(output)


@app.route('/users/<int:index>', methods = ['DELETE'])
def del_name(index):
    if index not in data:
        return "No Users", 204
    elif index in data:
        output = '{' + str(index) + ':' + data[index] + '}'
        del data[index]
        return "DELETE User {}".format(output), 204


def add_dict(x):
    global data
    i = len(data)
    data[i+1] = x









