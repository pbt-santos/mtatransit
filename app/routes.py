# import the app variable from the init file (which is in app dir)
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        # use the url_for to avoid errors and get it from function name annotation
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
