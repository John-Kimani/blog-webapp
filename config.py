import os

basedir = os.path.abspath(os.path.dirname(__file__))



class Config(object):
    '''
    General configuration class
    '''
    # RANDOM_QOUTES_URL = os.environ.get('QUOTES_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
    'postgres://', 'postgresql://') or\
    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #configuration to disable auto updates to database

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')