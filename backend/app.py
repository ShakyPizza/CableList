from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
import pandas as pd

app = Flask(__name__)
CORS(app)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for your Excel records (adjust column names as needed)
class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    column1 = db.Column(db.String(255))
    column2 = db.Column(db.String(255))
    column3 = db.Column(db.String(255))
    column4 = db.Column(db.String(255))
    column5 = db.Column(db.String(255))
    column6 = db.Column(db.String(255))
    column7 = db.Column(db.String(255))
    column8 = db.Column(db.String(255))
    column9 = db.Column(db.String(255))
    column10 = db.Column(db.String(255))

@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to upload and process an Excel file
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    df = pd.read_excel(file)

    # Optionally, clear previous records if needed
    db.session.query(Record).delete()
    for _, row in df.iterrows():
        record = Record(**{f"column{i+1}": str(row[i]) for i in range(10)})
        db.session.add(record)
    db.session.commit()
    return jsonify({"message": "File uploaded and processed"}), 200

# Endpoint to perform a search
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    if not query:
        return jsonify({"error": "No query provided"}), 400

    results = Record.query.filter(
        (Record.column1.ilike(f'%{query}%')) |
        (Record.column2.ilike(f'%{query}%')) |
        (Record.column3.ilike(f'%{query}%')) |
        (Record.column4.ilike(f'%{query}%')) |
        (Record.column5.ilike(f'%{query}%')) |
        (Record.column6.ilike(f'%{query}%')) |
        (Record.column7.ilike(f'%{query}%')) |
        (Record.column8.ilike(f'%{query}%')) |
        (Record.column9.ilike(f'%{query}%')) |
        (Record.column10.ilike(f'%{query}%'))
    ).all()

    return jsonify([{
        "id": r.id,
        "column1": r.column1,
        "column2": r.column2,
        "column3": r.column3,
        "column4": r.column4,
        "column5": r.column5,
        "column6": r.column6,
        "column7": r.column7,
        "column8": r.column8,
        "column9": r.column9,
        "column10": r.column10
    } for r in results])

if __name__ == '__main__':
    app.run(debug=True)