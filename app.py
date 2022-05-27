import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "welcome !"


@app.route("/aaa")
def hello():
    return "I am good, how about you ?"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
