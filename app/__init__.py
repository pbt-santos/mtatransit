from flask import Flask
from config import Config

# Flask extension wrappers
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager

# Logging 
import logging
# from logging.handlers import SMTPHandler, RotatingFileHandler
from logging.handlers import RotatingFileHandler
import os

# Create app and use route module
app = Flask(__name__)
app.config.from_object(Config)

# DB instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

# tell the app that the login page will handle view protection
login.login_view = 'login'


# log out to a file 10KB, showing timestamp alert level file loc
if not app.debug:

    # put other email logging here if required
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/mtatransit.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Starting up service')


# We're importing this here so that there isn't an issue from not declaring
# the above variable
from app import routes, models, errors

# log when not debugging and send to email if it is configured
#if not app.debug:
#    if app.config['MAIL_SERVER']:
#        auth = None
#        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
#            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
#        secure = None
#        if app.config['MAIL_USE_TLS']:
#            secure = ()
#
#        mail_handler = SMTPHandler(mailhost=(app.config['MAIL_SERVER'], 
#            app.config['MAIL_PORT']), fromaddr='no-reply@' + app.config['MAIL_SERVER'], 
#            toaddrs=app.config['ADMINS'], subject='Microblog Failure', 
#            credentials=auth, secure=secure)
#        mail_handler.setLevel(logging.ERROR)
#        app.logger.addHandler(mail_handler)
