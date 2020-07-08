from flask import Flask

# Create app and use route module
app = Flask(__name__)

from app import routes
