from flask import Flask
from app.config.settings import Config
from app.extensions import db, migrate
from app.api.routes import api_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app


   
