# This class will define our web forms for logins
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User


# Create the login form for the page
class LoginForm(FlaskForm):
    # Define our instance variables with initial values
    # DataRequired means that it cannot be submitted empty
    # a nice thing is that these all know how to render themselves in html
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


# Class that allows users to register themselves. WTForms checks email style
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # custom validators
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user: # name already exists
            raise ValidationError('Username already in use')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user: # email already exists
            raise ValidationError('Email already in use')

