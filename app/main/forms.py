
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired




class BlogForm(FlaskForm):
    '''
    Class that handles blog creation by admin
    '''
    blog_post = StringField('Enter blog post', validators=[DataRequired()])
    blog_title = StringField('Enter blog title', validators=[DataRequired()])
    submit = SubmitField('Submit Blog')


class SubscribeForm(FlaskForm):
    '''
    Class that handles subscription
    '''
    email = StringField('Enter your email', validators=[DataRequired()])
    username = StringField('Enter your username', validators=[DataRequired()])
