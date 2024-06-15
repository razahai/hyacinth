import os 
from flask import Blueprint, redirect, render_template, url_for, current_app
from werkzeug.utils import secure_filename

from hyacinth.apps.printing.forms import PrintRequestForm
from hyacinth.config import ALLOWED_FILE_TYPES, MAX_FILE_SIZE, MAX_PAGES_PER_JOB, PRINT_JOB_RATE_LIMIT

printing_bp = Blueprint("printing", __name__)

@printing_bp.route("/", methods=["GET", "POST"])
def index():
    form = PrintRequestForm()

    if form.validate_on_submit():
        print_job = form.print_job.data
        filename = secure_filename(print_job.filename)
        print_job.save(os.path.join(current_app.config["UPLOAD_PATH"], filename))
        return redirect(url_for("printing.index"))

    context = {
        "ALLOWED_FILE_TYPES": ALLOWED_FILE_TYPES,
        "MAX_FILE_SIZE": MAX_FILE_SIZE,
        "MAX_PAGES_PER_JOB": MAX_PAGES_PER_JOB,
        "PRINT_JOB_RATE_LIMIT": PRINT_JOB_RATE_LIMIT
    }

    return render_template("index.html", settings=context, form=form)