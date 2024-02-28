from flask import flash, redirect, url_for, Blueprint, render_template
from flask.views import View
from app.models import Album, Tour
from functools import wraps
from flask_login import current_user, login_required
from flask_babel import _

def admin_required(f):
    @wraps(f)
    def _admin_required(*args, **kwargs):
        if not current_user.is_admin:
            flash(_("You need to be an administrator to access this page"), "danger")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return _admin_required

admin = Blueprint("admin", __name__, template_folder="templates")

class TableView(View):
    decorators = [login_required, admin_required]

    def __init__(self, model):
        self.model = model
        self.columns = self.model.__mapper__.columns.keys()
        super(TableView, self).__init__()

    def dispatch_request(self):
        return render_template("resource_table.html",
                    instances=self.model.query.all(),
                    columns=self.columns,
                    resource_name=self.model.__name__.lower())

admin.add_url_rule("/album", view_func=TableView.as_view("album_table", model=Album))
admin.add_url_rule("/tour", view_func=TableView.as_view("tour_table", model=Tour))
