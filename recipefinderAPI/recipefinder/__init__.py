from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from recipefinder.config import Config
from flask_marshmallow import Marshmallow
from flask_cors import CORS


db = SQLAlchemy()
ma = Marshmallow()
cor = CORS()
bcrypt = Bcrypt()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    cor.init_app(app)
    from recipefinder.users.routes import users
    from recipefinder.recipes.routes import recipes
    app.register_blueprint(users)
    app.register_blueprint(recipes)
    return app
