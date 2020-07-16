''' This file will be used to define custom error handlers '''
from flask import render_template
from app import db
from app.errors import bp
# 400
# 403


# 404
@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


# 405


# 500 (usually caused when working with the db)
@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500

