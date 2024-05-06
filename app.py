from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/adduser', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    id = data.get('id')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create users table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        name TEXT,
                        id INTEGER
                    )''')

    cursor.execute("INSERT INTO users (name, id) VALUES (?, ?)", (name, id))
    conn.commit()

    cursor.execute("SELECT name FROM users WHERE id > 5")
    result = [row[0] for row in cursor.fetchall()]

    conn.close()

    return jsonify({"names_with_ids_above_5": result})

if __name__ == "__main__":
    app.run()


