''' This file will be used to define our database models:
    Users and Turnstiles (users optional for later)'''

from app import db

# Users of dashboard (more for following along with tutorial)
class User(db.Model):
    # Cols: id, username, email, passhash (security)
    # Type+length, indexed (searching), unique
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(80), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # essentially toString overloading
    def __repr__(self):
        return '<User {}>'.format(self.username)


# Class of the various groups in the station (an aggregate)
class TurnstileGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.String(64), nullable=False, index=True, unique=True)
    location = db.Column(db.String(50), nullable=False, unique=True)
    total_count = db.Column(db.Integer)
    total_rate = db.Column(db.Integer)
    turnstiles = db.relationship('Turnstile', backref='group', lazy='dynamic')

    def __repr__(self):
        return '<TurnstileGroup {}>'.format(group_id)


# Turnstile of Times square station 
class Turnstile(db.Model):
    # Cols: id, turnstile_id, group_id, turn_count, turn_rate (need anything else?)
    # May want to re-structure this later to have foreign keys fo r turnstile_id or group_id
    # Have turnstile_id as our main id and group_id just show location and other data?
    id = db.Column(db.Integer, primary_key=True)
    turnstile_id = db.Column(db.String(64), nullable=False, index=True, unique=True)
    turn_count = db.Column(db.Integer)
    turn_rate = db.Column(db.Float)
    group_id = db.Column(db.String(64), db.ForeignKey('turnstile_group.group_id'))

    def __repr__(self):
        return '<Turnstile {}, group {} has turn rate {}>'.format(self.turnstile_id, self.group_id, self.turn_rate)
