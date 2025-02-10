from flask import Flask
from flask_cors import CORS
from database import init_db
from routes import register_routes

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend interaction

# Initialize the database
init_db(app)

# Register API routes
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)  # Run in debug mode for development
