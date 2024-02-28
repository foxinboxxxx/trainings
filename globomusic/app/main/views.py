from flask import Blueprint, render_template, current_app
main=Blueprint("main", __name__, template_folder="templates")

# Home route
@main.route("/")
def home():
	return render_template("home.html")
