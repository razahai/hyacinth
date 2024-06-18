from flask import Blueprint, flash, g, redirect, render_template, session, url_for

from hyacinth.apps.auth.forms import LoginForm
from hyacinth.db.db import get_db

auth_bp = Blueprint("auth", __name__, url_prefix="/user")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if session.get("access_code"):
        return redirect(url_for("printing.index"))

    form = LoginForm()

    if form.validate_on_submit():
        access_code = form.access_code.data
        db = get_db()
        error = None
        user = db.execute(
            "SELECT * FROM users WHERE id = ?", (access_code,)
        ).fetchone()
        
        if user is None:
            error = "Incorrect access code"
        
        if error is None:
            session.clear()
            session["access_code"] = access_code
            return redirect(url_for("printing.index"))
        
        flash(error, "error")

    context = {
        "is_authenticated": False
    }

    return render_template("login.html", context=context, form=form)

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("printing.index"))