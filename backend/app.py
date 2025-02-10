import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_db_connection, init_db
from models import db, Cable

app = Flask(__name__)

# ✅ Allow only frontend domain (Fix CORS issue)
CORS(app, resources={r"/*": {"origins": "https://cable-list.vercel.app"}})

# ✅ Initialize Database
init_db()

@app.route("/")
def home():
    return "🚀 Flask App Running with MySQL and CORS Enabled!"

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
    # ✅ Use correct Flask port (5000 instead of 3306)
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
