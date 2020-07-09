from flask import Flask
from config import Config

# Create app and use route module
app = Flask(__name__)
app.config.from_object(Config)

# We're importing this here so that there isn't an issue from not declaring
# the above variable
from app import routes
