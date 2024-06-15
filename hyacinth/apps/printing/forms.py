from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms import SubmitField, ValidationError

from hyacinth.config import ALLOWED_FILE_TYPES, MAX_FILE_SIZE

class PrintRequestForm(FlaskForm):
    print_job = FileField(
        "Upload Print Job", 
        validators=[
            FileRequired(), 
            FileAllowed(ALLOWED_FILE_TYPES, "Please use one of the allowed file types")
        ]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField("Submit")

    def validate_print_job(form, field): 
        print_job = field.data

        if len(print_job.read()) > MAX_FILE_SIZE:
            raise ValidationError("This file is too large")

        print_job.seek(0) 