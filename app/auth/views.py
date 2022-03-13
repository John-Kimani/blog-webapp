from flask import render_template, redirect,url_for
from app.auth import auth
from app.auth.forms import LoginForm, RegisterForm



@auth.route('/login')
def login():
    '''
    View funciton that handles users log in
    '''
    form = LoginForm()
    title = 'LogIn'
    return render_template('auth/login.html', title=title, form=form)


@auth.route('/signup')
def signup():
    '''
    View function that handles user registration
    '''
    form = RegisterForm()
    title = 'Register'
    return render_template('auth/signup.html', title=title, form=form)