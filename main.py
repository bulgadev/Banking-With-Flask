from flask import Flask
from flask import request, jsonify
from flask import render_template, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("log.html")

if __name__ == "__main__":
    app.run()

