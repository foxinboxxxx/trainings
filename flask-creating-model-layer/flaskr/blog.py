from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from .auth import login_required
from .db import get_db
from .models.post import Post
from flaskr.sqla import sqla

bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    db = get_db()
    posts = Post.query.all()
    return render_template("blog/index.html", posts=posts)


def get_post(id, check_author=True):
    """Get a post and its author by id.

    Checks that the id exists and optionally that the current user is
    the author.

    :param id: id of post to get
    :param check_author: require the current user to be the author
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    #post = Post.query.get(id)
    post = Post.query.filter_by(id=id).first()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post.author_id != g.user.id:
        abort(403)

    return post


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    """Create a new post for the current user."""
    if request.method == "POST":
        try:
            post = Post(title=request.form['title'],body = request.form["body"],author_id = g.user.id)
        except ValueError as e:
            flash(str(e))
            return render_template("blog/create.html")

        """To save model into current SQLAlchemy session
        Add model to it and commit on the session
        SQLAl will attempt to write model to DB
        If constraint is violated, an exception will be raised
        Two step process: can add multiple new models and commit them in one go"""
        sqla.session.add(post)
        sqla.session.commit()
        return redirect(url_for("blog.index"))

    return render_template("blog/create.html")


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    """Update a post if the current user is the author."""
    post = get_post(id)

    """Replace validation with try-catch"""
    # if request.method == "POST":
    #     title = request.form["title"]
    #     body = request.form["body"]
    #     error = None

    #     if not title:
    #         error = "Title is required."

    #     if error is not None:
    #         flash(error)
    #     else:
    #         db = get_db()
    #         db.execute(
    #             "UPDATE post SET title = ?, body = ? WHERE id = ?", (title, body, id)
    #         )
    #         db.commit()
    #         return redirect(url_for("blog.index"))

    # return render_template("blog/update.html", post=post)
    if request.method == "POST":
        try:
            post.title = request.form["title"]
            post.body = request.form["body"]
        except ValueError as e:
            flash(str(e))
            return render_template("blog/update.html", post=post)
        
        sqla.session.add(post)
        sqla.session.commit()
        return redirect(url_for("blog.index"))

    return render_template("blog/update.html", post=post)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    """Delete a post.

    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    post=get_post(id)
    # db = get_db()
    # db.execute("DELETE FROM post WHERE id = ?", (id,))
    # db.commit()
    sqla.session.delete(post)
    sqla.session.commit()
    return redirect(url_for("blog.index"))
