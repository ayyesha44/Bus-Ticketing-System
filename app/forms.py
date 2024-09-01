from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo


class Loginform(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberme = BooleanField('Remember me')
    submit = SubmitField('Log in')

class Signupform(FlaskForm):
    email = StringField('Email address', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    retypepass = PasswordField('Retype password', validators=[DataRequired(), EqualTo('password')])
    signup = SubmitField('Sign up')