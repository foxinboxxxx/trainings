# Imports from Flask
from flask import Flask
# Other imports
import os
import config
# Import global extension variables
from app.extensions import *

basedir = os.path.abspath(os.path.dirname(__file__))
app_env = os.environ.get("FLASK_ENV")

def create_app(config_env=app_env):
    # Context objects pushed to stack automatically by Flask.
    # When the application instance gets created, both stacks are created too.
    # The request context is pushed whenever a new request comes in.
    app = Flask(__name__)
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

    # Initializing extensions
    init_extensions(app)

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
    from app.admin.views import admin
    app.register_blueprint(admin, url_prefix="/admin")

    # Imports for error pages
    from app.errors import page_not_found
    app.register_error_handler(404, page_not_found)

    # Imports for Jinja filters
    from app.filters import date_format
    app.add_template_filter(date_format)

    return app