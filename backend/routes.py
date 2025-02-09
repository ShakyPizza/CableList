from flask import Flask, request, jsonify, send_from_directory
import os
import pandas as pd
import sqlite3

app = Flask(__name__)

# Database configuration
DATABASE = "database.db"

def init_db():
    """Initialize the SQLite database and create the table if it doesn't exist."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cables (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            column1 TEXT,
            column2 TEXT,
            column3 TEXT,
            column4 TEXT
        )
        """)
        conn.commit()

@app.route("/upload", methods=["POST"])
def upload_file():
    """Upload an Excel file and save data to the database."""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        df = pd.read_excel(file)

        with sqlite3.connect(DATABASE) as conn:
            df.to_sql("cables", conn, if_exists="replace", index=False)

        return jsonify({"message": "File uploaded and data saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/search", methods=["GET"])
def search():
    """Search for data in the database."""
    query = request.args.get("q", "")

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cables WHERE column1 LIKE ?", ('%' + query + '%',))
        results = cursor.fetchall()

    return jsonify(results)

@app.route("/")
def serve_frontend():
    """Serve the frontend React app."""
    return send_from_directory("frontend/build", "index.html")

@app.route("/<path:path>")
def serve_static_files(path):
    """Serve static assets for the frontend."""
    return send_from_directory("frontend/build", path)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
