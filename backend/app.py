import os
from flask import Flask, request, jsonify
from db import get_db_connection, init_db

app = Flask(__name__)

# Ensure DB is initialized
init_db()

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