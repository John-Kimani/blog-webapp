from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    '''
    Initialize requirements
    '''
    db.init_app(app)
    migrate.init_app(app, db)

    '''
    Registering main blueprint
    '''
    from app.main import main as main_bp
    app.register_blueprint(main_bp)
    '''
    Registering error blueprint
    '''
    from app.errors import error as errors_bp
    app.register_blueprint(errors_bp)
    '''
    Registering auth blueprint
    '''
    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix= '/authenticate')



    return app