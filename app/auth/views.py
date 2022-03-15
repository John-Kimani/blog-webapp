from flask import flash, render_template, redirect,url_for,request
from flask_login import login_user,logout_user, current_user
from app.auth import auth
from app.auth.forms import LoginForm, RegisterForm
from app import db

from app.models import Admin



@auth.route('/login', methods=['GET','POST'])
def login():
    '''
    View funciton that handles users log in
    '''
    if current_user.is_authenticated:
        '''
        Redirects logged in user to home page
        '''
        return redirect(url_for('main.createblog'))
    form = LoginForm()
    title = 'LogIn'
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        print(admin)
        if admin is None or not admin.check_password(form.password.data):
            '''
            Condition to handle invalid user input
            Returns:
                Invalid response retains user on login page to enable them try again
                Valid reponse redirects user to the authorized home page
            '''
            flash('Invalid username or password')
            return redirect( url_for('auth.login'))
        login_user(admin, remember=form.remember_me.data)
        flash('You are logged in successfully')
        return redirect(url_for('main.createblog'))
    return render_template('auth/login.html', title=title, form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    '''
    View function that handles user registration
    '''
    if current_user.is_authenticated:
        '''
        logic that validates user session
        '''
        return redirect(url_for('index'))
    title = 'Register'
    form = RegisterForm()
    if form.validate_on_submit():
        print('start')
        admin = Admin(username=form.username.data, email=form.email.data)
        admin.set_password(form.password.data)
        db.session.add(admin)
        db.session.commit()
        flash('Welcome a board')
        return redirect(url_for('main.createblog'))
    else: 
        print(form.data)
        print('Not working yet')
    print(request.method)
    return render_template('auth/signup.html', title=title, form=form)


@auth.route('/logout')
def logout():
    '''
    View function that handles log out
    '''
    logout_user()
    return redirect(url_for('auth.login'))