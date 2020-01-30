#!flask/bin/python
import flask
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return flask.jsonify({"data":"Hello World"}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
