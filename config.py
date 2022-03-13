import os


class Config(object):
    '''
    General configuration class
    '''
    RANDOM_QOUTES_URL = os.environ.get('QUOTES_URL')