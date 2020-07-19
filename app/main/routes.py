# import the app variable from the init file (which is in app dir)
from flask import render_template, flash, redirect, url_for, request, g, jsonify, current_app
from app import db
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Turnstile, TurnstileGroup
from app.main import bp
import json
from app.data.utils import TurnstileExtractor

# let's create a provisional before request section
# @app.before_request
# def before_request():
#     pass

extractor = TurnstileExtractor("./app/data/turnstile_data.csv")


# Show this whenever we hit these two endpoints but make people login
@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    # mock data before first upload
    turnstiles = [
        {
            'turnstile_id': '1', 
            'net_entry': '2',
            'net_exit': '5'
            #'turn_rate': '0.5'
        },
        {
            'turnstile_id': '2', 
            'net_entry': '2',
            'net_exit': '7'
            #'turn_rate': '1'
        }
    ]
    return render_template('index.html', title='Home', turnstiles=turnstiles)


# route to get the table data every 5 seconds. Would need to add security in a real application
@bp.route('/data', methods=['GET'])
def get_data():
    # we will later get this data from pandas
    #turnstiles = [
    #    {
    #        'turnstile_id': '1', 
    #        'net_entry': '2',
    #        'net_exit': '5'
    #        #'turn_rate': '0.5'
    #    },
    #    {
    #        'turnstile_id': '2', 
    #        'net_entry': '2',
    #        'net_exit': '7'
    #        #'turn_rate': '1'
    #    }
    #]
    #return json.dumps(turnstiles)
    jsonRet = extractor.retrieve_next_minute()
    return jsonRet

# route to display an alert about turnstile
@bp.route('/alert', methods=['POST'])
def alert_turnstile():
    flash('Worker dispatched to check turnstile', 'error')
