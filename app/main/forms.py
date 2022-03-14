
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length




class BlogForm(FlaskForm):
    '''
    Class that handles blog creation by admin
    '''
    blog_post = StringField('Enter blog post', validators=[DataRequired()])
    blog_title = StringField('Enter blog title', validators=[DataRequired()])
    submit = SubmitField('Submit Blog')