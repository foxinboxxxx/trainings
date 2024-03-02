from flask import Blueprint

url_processors = Blueprint("url_processors", __name__)

# Always add app prefix to attach the app instance
# to avoid exec before view functions to the blueprint
@url_processors.app_url_value_preprocessor
def processor(endpoint, values):
    return

@url_processors.app_url_defaults
def defaults_processor(endpoint, values):
    return
