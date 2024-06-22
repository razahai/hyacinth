from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms import MultipleFileField, SubmitField, ValidationError

from hyacinth.config import ALLOWED_FILE_TYPES, MAX_FILE_SIZE, MAX_PAGES_PER_JOB

class PrintRequestForm(FlaskForm):
    print_job = MultipleFileField(
        "Upload Print Job", 
        validators=[
            FileRequired(), 
            FileAllowed(ALLOWED_FILE_TYPES, "Please use one of the allowed file types")
        ]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField("Submit")

    def validate_print_job(form, field): 
        if len(field.data) > MAX_PAGES_PER_JOB:
            raise ValidationError("Too many files!")
        
        for print_job in field.data:
            if len(print_job.read()) > MAX_FILE_SIZE:
                raise ValidationError("One of these files are too large")
            print_job.seek(0) 