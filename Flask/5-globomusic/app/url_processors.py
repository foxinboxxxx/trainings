from flask import Blueprint, g, current_app, after_this_request, request

url_processors = Blueprint("url_processors", __name__)

@url_processors.before_app_request
def before_request():
    # check if request for static file like CSS or JS
    # static files dont need lang
    if request.endpoint is "static":
        return
    if request.cookies.get("lang") != g.lang:
        @after_this_request
        def set_cookie(response):
            response.set_cookie("lang", g.lang, max_age=60*60*24*100)
            return response


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
        if endpoint is "static":
            return
        g.lang = values.pop("lang")
    except:
        if (
                request.cookies.get("lang") and
                request.cookies.get("lang") in current_app.config["LANGUAGES"]
            ):
            g.lang = request.cookies.get("lang")
        else:
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