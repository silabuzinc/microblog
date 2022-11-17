from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.models.posts import Post
from app.models.usuarios import User
from app.models.roles import Role


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(Config)

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    return app
