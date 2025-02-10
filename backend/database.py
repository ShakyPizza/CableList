from flask_sqlalchemy import SQLAlchemy
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

db = SQLAlchemy()  # Initialize SQLAlchemy instance

def get_db_uri():
    """Returns the database URI based on environment settings."""
    if DB_USER and DB_PASSWORD:  # If using PostgreSQL/MySQL
        return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return f"sqlite:///{DB_NAME}"  # Default to SQLite

def init_db(app):
    """Configures and initializes the database with Flask."""
    app.config["SQLALCHEMY_DATABASE_URI"] = get_db_uri()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)  # Bind database to Flask app

    with app.app_context():
        db.create_all()  # Create tables if they don't exist
