from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate

def create_app():
    # Import blueprints inside the function to avoid circular imports
    from routes.auth import auth_bp
    from routes.main import main_bp

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp, url_prefix="/")

    return app
