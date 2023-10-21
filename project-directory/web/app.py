from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/data", methods=["POST"])
def add_data():
    data = request.json
    conn = psycopg2.connect(
        dbname = "mydatabase",
        user = "myuser",
        password = "mypassword",
        host = "db"
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data (name) VALUES (%s)", (data[{name}],))
