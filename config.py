# In this file we're going to define our app configs as a class
# We'll be using flask forms to authenticate our dashboard users (optional functionality display)
import os

# To get our environment variables automatically set
from dotenv import load_dotenv

# Fallback location of database in app main dir
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# we're going to use this rather than app.config so that it is separate
class Config(object):
    # using this with one of the imports will help protect from some attacks
    # Idea is to take information from environment variables when possible
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'myKey'

    # Database (from environ or app.db file)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # Don't signal the database when about to make modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Add some notifications in case errors occur
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['mtaadmin@mta.gov'] # this is just an example
