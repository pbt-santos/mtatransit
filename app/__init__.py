from flask import Flask
from config import Config

# Flask extension wrappers
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager

# Create app and use route module
app = Flask(__name__)
app.config.from_object(Config)

# DB instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

# We're importing this here so that there isn't an issue from not declaring
# the above variable
from app import routes, models
