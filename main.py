from flask import Flask
from flask import render_template, redirect, request, jsonify
import sqlite3
import bcrypt

conn = sqlite3.connect("my_database.db", check_same_thread=False)  # Allow connection sharing across threads
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, balance REAL DEFAULT 0.0)")
conn.commit()

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def tryreg(username, hpassword):
    try:
        cursor.execute("INSERT INTO users (username, password, balance) VALUES (?, ?, ?)", (username, hpassword, 0.0))
        conn.commit()
    except sqlite3.IntegrityError:
        return render_template("register.html", error="Username already exists")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("log.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        hpassword = hash_password(password)
        tryreg(username, hpassword)

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
