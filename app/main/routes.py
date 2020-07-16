# import the app variable from the init file (which is in app dir)
from flask import render_template, flash, redirect, url_for, request, g, jsonify, current_app
from app import db
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Turnstile, TurnstileGroup
from app.main import bp
import json

# let's create a provisional before request section
# @app.before_request
# def before_request():
#     pass


# Show this whenever we hit these two endpoints but make people login
@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    # Let's mock some turnstyle data. This will later come from a SQL database
    # the following will be the username of the station worker
    turnstiles = [
        {
            'turnstile_id': '1', 
            'group_id': '2',
            'turn_count': '5',
            'turn_rate': '0.5'
        },
        {
            'turnstile_id': '2', 
            'group_id': '2',
            'turn_count': '7',
            'turn_rate': '1'
        }
    ]
    return render_template('index.html', title='Home', turnstiles=turnstiles)


# route to get the table data every 5 seconds. Would need to add security in a real application
@bp.route('/data', methods=['GET'])
def get_data():
    # we will later get this data from pandas
    turnstiles = [
        {
            'turnstile_id': '1', 
            'group_id': '2',
            'turn_count': '5',
            'turn_rate': '0.5'
        },
        {
            'turnstile_id': '2', 
            'group_id': '2',
            'turn_count': '7',
            'turn_rate': '1'
        }
    ]
    return json.dumps(turnstiles)
