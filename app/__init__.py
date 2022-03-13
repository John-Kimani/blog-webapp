from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    '''
    Initialize requirements
    '''
    bootstrap.init_app(app)

    '''
    Registering main blueprint
    '''
    from app.main import main as main_bp
    app.register_blueprint(main_bp)



    return app