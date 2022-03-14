from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class LoginForm(FlaskForm):
    '''
    Classs that handles user login
    '''
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log In')


class RegisterForm(FlaskForm):
    '''
    class that handles user registration
    '''
    username = StringField('Username', validators=[DataRequired(), Length(1,20)])
    email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()