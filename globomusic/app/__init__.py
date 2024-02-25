# Imports from Flask
from flask import Flask
# Extension for implementing SQLAlchemy ORM
from flask_sqlalchemy import SQLAlchemy
# Extension for implementing Flask-Login for authentication
from flask_login import LoginManager
# Extension for implementing translations
from flask_babel import Babel, _
from flask_babel import lazy_gettext as _l
# Other imports
import os
import config

basedir = os.path.abspath(os.path.dirname(__file__))
# extensions as globals
db = SQLAlchemy()
#Babel is used for translation
babel = Babel()
login_manager = LoginManager()

def create_app(config_env=""):
    # Context objects pushed to stack automatically by Flask.
    # When the application instance gets created, both stacks are created too.
    # The request context is pushed whenever a new request comes in.
    app = Flask(__name__)
    if not config_env:
        config_env = app.env
    app.config.from_object("config.{}Config".format(app.env.capitalize()))
    # app.config.from_mapping(
    #     SECRET_KEY=os.environ.get("FLASK_SECRET_KEY") or "prc9FWjeLYh_KsPGm0vJcg",
    #     SQLALCHEMY_DATABASE_URI="sqlite:///"+ os.path.join(basedir, "globomantics.sqlite"),
    #     SQLALCHEMY_TRACK_MODIFICATIONS=False,
    #     MAX_CONTENT_LENGTH=16*1024*1024,
    #     IMAGE_UPLOADS=os.path.join(basedir, "uploads"),
    #     ALLOWED_IMAGE_EXTENSIONS=["jpeg", "jpg", "png"]
    # )
    print("Config " + str("config.{}Config".format(config_env.capitalize())))

    # DON'T DO THIS EVER EVER!!!!
    # app.config["ENV"] = "testing"

    # Initializing extensions when factory is executing
    db.init_app(app)
    babel.init_app(app)
    login_manager.init_app(app)


    login_manager.login_view = "auth.login"
    login_manager.session_protection = "strong"
    login_manager.login_message = _l("You need to be logged in to access this page.")
    login_manager.login_message_category = "danger"

    # Avoid working outside of application context error
    with app.app_context():
        from app.album.views import album
        app.register_blueprint(album, url_prefix="/album")
        from app.main.views import main
        app.register_blueprint(main)
    from app.auth.views import auth
    app.register_blueprint(auth)
    from app.tour.views import tour
    app.register_blueprint(tour, url_prefix="/tour")

    from app.main.views import page_not_found
    app.register_error_handler(404, page_not_found)

    return app