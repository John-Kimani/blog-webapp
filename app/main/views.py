from flask import render_template, redirect,url_for
from app.main import main
from app.request import get_random_qoutes



@main.route('/')
@main.route('/index')
def index():
    '''
    View function that sets index page
    '''
    title = 'Home'
    random_quote = get_random_qoutes()

    return render_template('index.html', title=title, quotes=random_quote)