from flask import Flask
from flask import render_template
from flask import request
flsk = Flask(__name__)


@flsk.route("/")
def hello_world():
    return "hello world"


@flsk.route("/user/<user_name>")
def name(user_name):
    return f"Hello {user_name}"


@flsk.route("/template")
def template():
    return render_template("index.html")


@flsk.route("/data", methods=['GET', 'POST'])
def getting_data():
    a = request.data
    print(type(a))
    return request.data


if __name__ == '__main__':
    flsk.run(debug=True, host="0.0.0.0")
