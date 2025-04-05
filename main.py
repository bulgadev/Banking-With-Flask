from flask import Flask
from flask import render_template, redirect, request, jsonify, session, url_for
import sqlite3
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')





conn = sqlite3.connect("my_database.db", check_same_thread=False)  # Allow connection sharing across threads
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, balance REAL DEFAULT 0.0)")
conn.commit()

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def check_password(password_attempt, stored_hash):
    return bcrypt.checkpw(password_attempt.encode(), stored_hash.encode('utf-8'))

def tryreg(username, hpassword):
    try:
        cursor.execute("INSERT INTO users (username, password, balance) VALUES (?, ?, ?)", (username, hpassword, 0.0))
        conn.commit()
    except sqlite3.IntegrityError:
        return render_template("register.html", error="Username already exists")
    
def trylog(username, password):
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    fetch = cursor.fetchone()

    if fetch is None:
        print("User not found")
        return render_template("log.html", error="User not found")
        
    stored = fetch[0]

    if check_password(password, stored):
        session['username'] = username
        print(f"Welcome back {username}")
        return redirect("/dashboard")
    else:
        print("Incorrect password")
    
def check_balance():
    username = session['username']
    cursor.execute("SELECT balance FROM users WHERE username = ?", (username,))
    balance = cursor.fetchone()
    return balance

def withdraw():
    username = session['username']
    try:
        amount = float(request.form.get("amount"))
    except:
        return "Invalid Amount", 400
    cursor.execute("UPDATE users SET balance = balance - ? where USERNAME = ?", (amount, username))
    conn.commit()

def deposit():
    username = session['username']
    try:
        amount = float(request.form.get("amountd"))
    except:
        return "Invalid Amount", 400
    cursor.execute("UPDATE users SET balance = balance + ? where USERNAME = ?", (amount, username))
    conn.commit()


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        return trylog(username, password)

    return render_template("log.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        hpassword = hash_password(password)
        tryreg(username, hpassword)

    return render_template("register.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if 'username' not in session:
        return redirect("/login")

    username = session['username']

    if request.method == "POST":
        if 'amount' in request.form:
            withdraw()
        elif 'amountd'in request.form:
            deposit()

    balance = check_balance()[0]
    return render_template("dashboard.html", username=username, balance=balance)


if __name__ == "__main__":
    app.run(debug=True)

