from flask import session, Blueprint, render_template, flash, redirect, url_for, g
from app.auth.forms import RegistrationForm
from app import db
from app.models import User
from app.auth.forms import LoginForm
from werkzeug.local import LocalProxy

auth = Blueprint("auth", __name__, template_folder="templates")

current_user = LocalProxy(lambda: get_current_user())

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user.check_password(password):
            flash("Successfully logged in", "success")
            login_user(user)
            return redirect(url_for("main.home"))
        else:
            form.password.errors.append("Password is incorrect")

    return render_template("login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    # if session.get("user_id"):
    #     current_user = User.query.get(session.get("user_id"))
    #     flash("You already login " + current_user.username, "danger")

    form = RegistrationForm()

    if form.validate_on_submit():
        username    = form.username.data
        email       = form.email.data
        password    = form.password.data
        location    = form.location.data
        description = form.description.data

        user = User(username, email, password, location, description)
        db.session.add(user)
        db.session.commit()
        flash("You are registered", "success")
        return redirect(url_for("main.home"))

    return render_template("register.html", form=form)

@auth.route("/logout")
def logout():
    #if not session.get("user_id"):
    if current_user.is_anonymous():
        flash("You are not logged in", "danger")
    else:
        logout_user()
        flash("You are logger out", "success")
    return redirect(url_for("main.home"))

def login_user(user):
    session["user_id"] = user.id

def logout_user():
    session.pop("user_id")

@auth.app_context_processorcontext_processor
def inject_current_user():
    return dict(current_user=get_current_user())

def get_current_user():
    # Eliminate multiple call to DB during one page view
    _current_user =getattr(g, "_current_user", None)
    if _current_user is None and session.get("user_id"):
        user =User.query.get(session.get("user_id"))
        if user:
            _current_user=g._current_user.user
    
    if _current_user is None:
        _current_user=User()
    return _current_user