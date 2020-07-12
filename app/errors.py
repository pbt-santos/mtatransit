''' This file will be used to define custom error handlers '''
from flask import render_template
from app import app, db

# 400
# 403


# 404
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


# 405


# 500 (usually caused when working with the db)
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

