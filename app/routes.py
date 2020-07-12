# import the app variable from the init file (which is in app dir)
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse


# let's create a provisional before request section
# @app.before_request
# def before_request():
#     pass


# Show this whenever we hit these two endpoints but make people login
@app.route('/')
@app.route('/index')
@login_required
def index():
    # Let's mock some turnstyle data. This will later come from a SQL database
    # the following will be the username of the station worker
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
    return render_template('index.html', title='Home', turnstiles=turnstiles)


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

        # parse url to get to page we were redirected from (from url)
        next_page = request.args.get('next')

        # If login url doesn't have the next query string section, goto index
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


# Add a way to logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# Registration page for new users
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('New user registered ({})'.format(user.username))
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
