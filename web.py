# Flask Mega-Tutorial
# Parts 1-12 of 23

# Uses SQLite database
# Uses Werkzeug for password security

from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
