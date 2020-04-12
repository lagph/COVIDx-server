from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os

from config import app_config


db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    if os.getenv("FLASK_CONFIG") == "production":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
        )
    else:
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config_name])
        app.config.from_pyfile('config.py')

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You need to be logged in."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

    @app.route("/")
    def homepage():
        return "homepage"

    from models import user

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix="/admin")

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app