from flask import flash, render_template, redirect,url_for
from flask_login import login_user,logout_user, current_user
from app.auth import auth
from app.auth.forms import LoginForm, RegisterForm
from app import db

from app.models import User



@auth.route('/login', methods=['GET','POST'])
def login():
    '''
    View funciton that handles users log in
    '''
    if current_user.is_authenticated:
        '''
        Redirects logged in user to home page
        '''
        return redirect(url_for('main.index'))
    form = LoginForm()
    title = 'LogIn'
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            '''
            Condition to handle invalid user input
            Returns:
                Invalid response retains user on login page to enable them try again
                Valid reponse redirects user to the authorized home page
            '''
            flash('Invalid username or password')
            return redirect( url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        flash('You are logged in successfully')
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', title=title, form=form)


@auth.route('/signup')
def signup():
    '''
    View function that handles user registration
    '''
    if current_user.is_authenticated:
        '''
        logic that validates user session
        '''
        return redirect(url_for('main.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username= form.username.data, email=form.email.data, password_hash=form.password.data)
        '''
        condition that creates a new user and adds user to db
        '''
        user.set_password(form.password.data) #handles password hashing
        db.session.add(user)
        db.session.commit()
        flash('Congratulations you are now part of our commmunity')
        return redirect('auth.login')
    title = 'Register'
    return render_template('auth/signup.html', title=title, form=form)


@auth.route('/logout')
def logout():
    '''
    View function that handles log out
    '''
    logout_user()
    return redirect(url_for('main.index'))