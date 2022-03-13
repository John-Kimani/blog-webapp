from app import create_app,db

from app.models import Admin, Blog


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'Admin':Admin, 'Blog':Blog}