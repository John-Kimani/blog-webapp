from flask import render_template, redirect,url_for
from app.main import main
from app.request import get_random_qoutes
from app.main.forms import LoginForm, RegisterForm



@main.route('/')
@main.route('/index')
def index():
    '''
    View function that sets index page
    '''
    title = 'Home'
    random_quote = get_random_qoutes()

    return render_template('index.html', title=title, quotes=random_quote)

@main.route('/login')
def login():
    '''
    View funciton that handles users log in
    '''
    form = LoginForm()
    title = 'LogIn'
    return render_template('auth/login.html', title=title, form=form)


@main.route('/signup')
def sigup():
    '''
    View function that handles user registration
    '''
    form = RegisterForm()
    title = 'Register'
    return render_template('auth/signup.html', title=title, form=form)
    