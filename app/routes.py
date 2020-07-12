# import the app variable from the init file (which is in app dir)
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User


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


# generate the view for the login form and tell the controller to accept various methods 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        # get the data returned by searching for our username against form data
        user = User.query.filter_by(username=form.username.data).first()
        # Let's now do some error checking
        if not user or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        # Success
        login_user(user, remember=form.remember_me.data)
        # use the url_for to avoid errors and get it from function name annotation
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


# Add a way to logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
