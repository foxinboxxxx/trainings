from flask import Blueprint, g, current_app

url_processors = Blueprint("url_processors", __name__)

# Always add app prefix to attach the app instance
# to avoid exec before view functions to the blueprint
@url_processors.app_url_value_preprocessor
def pull_lang_code(endpoint, values):
    #print("Endpoint: " + endpoint)
    #print("Values: " + str(values))
    #return

    # processor willl put lang code from route to this g object
    # and get_locate fun will return value to babel
    try:
        g.lang = values.pop("lang")
    except:
        g.lang = current_app.config["LANGUAGES"][0]

@url_processors.app_url_defaults
def add_language_code(endpoint, values):
    #values['slug'] = 'tlak-to-docker-tome'
    #return
    if "lang" in values:
        return
    # current_app is proxy
    if current_app.url_map.is_endpoint_expecting(endpoint, "lang"):
        values["lang"] = g.lang