import os


class Config(object):
    '''
    General configuration class
    '''
    # RANDOM_QOUTES_URL = os.environ.get('QUOTES_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'