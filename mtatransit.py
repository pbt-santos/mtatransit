# This will be the main application module
from app import app, db
from app.models import Turnstile, TurnstileGroup, User

# we will later do some logging with this

# let's configure stuff to work with flask shell when testing db
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Turnstile': Turnstile, 'TurnstileGroup': TurnstileGroup }
