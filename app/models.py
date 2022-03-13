from . import db



class Quote:
    '''
    Class that defines quote 
    '''

    def __init__(self, author, quote_message):
        self.author = author 
        self.quote_message = quote_message 




class Admin(db.Model):
    '''
    Class that defines admin/writer priviledge
    Args: base class for all models from flask-sqlalchemy
    '''
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(120))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'Admin {self.username}'