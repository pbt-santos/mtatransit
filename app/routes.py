# import the app variable from the init file (which is in app dir)
from app import app

# Show this whenever we hit these two endpoints
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
