from flask import render_template, redirect,url_for
from app.main import main




@main.route('/')
@main.route('/index')
def index():
    '''
    View function that sets index page
    '''
    title = 'Home'


    return render_template('index.html', title=title)