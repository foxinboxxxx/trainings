from flask import Blueprint, render_template
from app import app
main=Blueprint("main", __name__, template_folder="templates")

# Home route
@main.route("/")
def home():
	return render_template("home.html")

# 404 error handler
#@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html")