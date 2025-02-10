import os
from flask import Flask, request, jsonify
from db import get_db_connection, init_db
from flask_cors import CORS
from models import db, Cable, init_db






app = Flask(__name__)
CORS(app)  # Allow frontend to access backend
init_db(app)


@app.route("/")
def home():
    return "🚀 Flask App Running with MySQL!"


@app.route("/search", methods=["GET"])
def search():
    """Search the MySQL database."""
    query = request.args.get("q", "")
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cables WHERE column1 LIKE %s", ('%' + query + '%',))
    results = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 3306)), debug=True)