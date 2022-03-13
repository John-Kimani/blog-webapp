from app.errors import error
from flask import render_template




@error.app_errorhandler(404)
def not_found(error):
    '''
    Function that handles page not found error
    '''
    return render_template('errors/404.html'), 404