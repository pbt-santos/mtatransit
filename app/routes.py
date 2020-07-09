# import the app variable from the init file (which is in app dir)
from flask import render_template
from app import app

# Show this whenever we hit these two endpoints
@app.route('/')
@app.route('/index')
def index():
    # Let's mock some turnstyle data. This will later come from a SQL database
    # the following will be the username of the station worker
    user = {'username': 'tester'}
    turnstiles = [
        {
            'id': '1', 
            'group': '2',
            'turn_count': '5',
            'turn_rate': '0.5'
        },
        {
            'id': '2', 
            'group': '2',
            'turn_count': '7',
            'turn_rate': '1'
        }
    ]
    return render_template('index.html', title='Home', user=user, turnstiles=turnstiles)
