from flask import Flask
from Test import Test
from flask import jsonify

app = Flask(__name__)

app.debug = True

t = Test()

@app.route('/')
def home():
    state = {
        "dpp": "doo",
        "val": 10,
        "v": t.get(10)
    }
    return jsonify(state)

@app.route("/test")
def test():
    return "Another route"

@app.route("/test3")
def test1():
    return "Test 3"