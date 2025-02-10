import os
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from db import get_db_connection, init_db
from models import db, Cable

app = Flask(__name__)

# ✅ Allow only frontend domain (Fix CORS issue)
CORS(app, resources={r"/*": {"origins": "https://cable-list.vercel.app"}})

# ✅ Initialize Database
init_db()

# ✅ Set Upload Folder
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"xlsx", "xls"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Check if the file extension is allowed."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["POST"])
def upload_file():
    """Handle file upload and process Excel data."""
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        # ✅ Process Excel file and store in database
        try:
            df = pd.read_excel(file_path)
            conn = get_db_connection()
            df.to_sql("cables", conn, if_exists="replace", index=False)
            conn.close()
            return jsonify({"message": "File uploaded and data saved successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Invalid file type"}), 400

@app.route("/")
def home():
    return "🚀 Flask App Running with MySQL and CORS Enabled!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
