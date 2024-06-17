from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    access_code = StringField("Access Code", validators=[DataRequired()])
    submit = SubmitField("Sign In")