# Imports from Flask
from flask import render_template, flash, url_for, redirect
# Extension for implementing Flask-Login for authentication
from flask_login import current_user, login_required, login_user, logout_user
# Extension for implementing translations
from flask_babel import _
from flask_babel import lazy_gettext as _l
# Other imports
import os
import datetime
from app import app, db
from app.models import User
from app.auth.forms import RegistrationForm, LoginForm


# Route for registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()

    if form.validate_on_submit():
        username    = form.username.data
        email       = form.email.data
        password    = form.password.data

        user = User(username, email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash(_("You are registered."), "success")
        login_user(user)
        return redirect(url_for("home"))

    return render_template("register.html", form=form)

# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(_("Invalid username or password"))
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("home"))

    return render_template("login.html", form=form)

# Logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


