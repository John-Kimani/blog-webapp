from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin



class Quote:
    '''
    Class that defines quote 
    '''

    def __init__(self, author, quote_message):
        self.author = author 
        self.quote_message = quote_message 

@login.user_loader
def load_user(id):
    '''
    Function that handles logged in user in each admin session
    '''
    return Admin.query.get(int(id))


class Admin(UserMixin,db.Model):
    '''
    Class that defines admin/writer priviledge
    Args: base class for all models from flask-sqlalchemy
    '''
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(120))
    password_hash = db.Column(db.String(128))
    blogs = db.relationship('Blog', backref='writter', lazy='dynamic')

    def __repr__(self):
        '''
        Funtion that print out admins infomation
        '''
        return '<Admin {}>'.format(self.username)

    def set_password(self, password):
        '''
        Function that sets password
        '''
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        '''
        Function to check the admnis password 
        '''
        return check_password_hash(self.password_hash, password)

class Blog(db.Model):
    '''
    class that instanciates blog posts
    '''
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key = True)
    blog_title = db.Column(db.String(25))
    blog_post = db.Column(db.String(300))
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    timestamp = db.Column(db.DateTime, index = True, default=datetime.utcnow)
    
    def __repr__(self):
        return f'Blog {self.blog_post}'

class User(db.Model):
    '''
    Class that instanctiates users interactions
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique = True, index = True)
    comments = db.relationship('Comment', backref='user', lazy=True)

    def __repr__(self):
        return f'User {self.username}'


class Comment(db.Model):
    '''
    Class that instanciates comments made by users
    '''
    __tablename__ = 'Comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text())
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Comment {self.comment}'