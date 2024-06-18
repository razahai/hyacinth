import os 
from flask import Blueprint, flash, redirect, render_template, session, url_for, current_app
from werkzeug.utils import secure_filename

from hyacinth.apps.printing.forms import PrintRequestForm
from hyacinth.config import ALLOWED_FILE_TYPES, MAX_FILE_SIZE, MAX_PAGES_PER_JOB, PRINT_JOB_RATE_LIMIT, REQUEST_FORM
from hyacinth.db.db import get_db

printing_bp = Blueprint("printing", __name__)

@printing_bp.route("/", methods=["GET", "POST"])
def index():
    form = PrintRequestForm()
    access_code = session.get("access_code")

    if form.validate_on_submit():
        if not access_code:
            flash("You must be logged in to submit a print job request", "error")
        else:
            db = get_db()
            
            print_job = form.print_job.data
            filename = f"{access_code}_{secure_filename(print_job.filename)}"
            print_job.save(os.path.join(current_app.config["UPLOAD_PATH"], filename))

            db.execute(
                "INSERT INTO jobs (user_id, file_name, job_status) VALUES (?, ?, ?)",
                (access_code, filename, "pending")
            )
            db.commit()

            flash("Successfully submitted print job request!", "success")
        return redirect(url_for("printing.index"))

    overall_job_count, user_job_count, overall_pending_jobs, overall_ip_jobs = get_job_data(access_code)

    context = {
        "ALLOWED_FILE_TYPES": ALLOWED_FILE_TYPES,
        "MAX_FILE_SIZE": MAX_FILE_SIZE,
        "MAX_PAGES_PER_JOB": MAX_PAGES_PER_JOB,
        "PRINT_JOB_RATE_LIMIT": PRINT_JOB_RATE_LIMIT,
        "REQUEST_FORM": REQUEST_FORM,
        "is_authenticated": bool(access_code),
        "overall_jobs": overall_job_count,
        "user_jobs": user_job_count,
        "pending_jobs": overall_pending_jobs,
        "in_progress_jobs": overall_ip_jobs
    }

    return render_template("index.html", context=context, form=form)

def get_job_data(access_code):
    db = get_db()

    result = db.execute(
        """
        SELECT 
            (SELECT COUNT(*) FROM jobs) AS overall_job_count, 
            (SELECT COUNT(*) FROM jobs WHERE user_id = ?) AS user_job_count,
            (SELECT COUNT(*) FROM JOBS WHERE job_status = 'pending') AS overall_pending_jobs,
            (SELECT COUNT(*) FROM JOBS WHERE job_status = 'in_progress') AS overall_ip_jobs;
        """,
        (access_code,)
    ).fetchone()

    return result