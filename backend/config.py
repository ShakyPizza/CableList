import os

class Config:
    """Base configuration with defaults."""
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Use MySQL/PostgreSQL if DATABASE_URL is set, otherwise fallback to SQLite
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///instance/data.db")

class DevelopmentConfig(Config):
    """Development-specific configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production-specific configuration."""
    DEBUG = False

# Select config based on environment
ENV = os.getenv("FLASK_ENV", "development")  # 'development' or 'production'
if ENV == "production":
    config = ProductionConfig()
else:
    config = DevelopmentConfig()
