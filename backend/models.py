from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cable(db.Model):
    """Model for storing cable data."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    column1 = db.Column(db.String(255), nullable=False)
    column2 = db.Column(db.String(255), nullable=True)
    column3 = db.Column(db.String(255), nullable=True)
    column4 = db.Column(db.String(255), nullable=True)

def init_db(app):
    """Initialize the database."""
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"  # Update with MySQL if needed
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        print("✅ Database tables created!")
