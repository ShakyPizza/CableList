import os

# Database configuration
DB_NAME = os.getenv("DB_NAME", "cables.db")
DB_USER = os.getenv("DB_USER", "root")  # If using MySQL/PostgreSQL
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")  # Default for PostgreSQL

# Flask settings
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# CORS settings
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")
