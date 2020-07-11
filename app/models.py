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

# Turnstile of Times square station 
class Turnstile(db.Model):
    # Cols: id, turnstile_id, group_id, turn_count, turn_rate (need anything else?)
    # May want to re-structure this later to have foreign keys fo r turnstile_id or group_id
    # Have turnstile_id as our main id and group_id just show location and other data?
    id = db.Column(db.Integer, primary_key=True)
    turnstile_id = db.Column(db.String(64), nullable=False, index=True, unique=True)
    group_id = db.Column(db.String(64), nullable=False, index=True)
    turn_count = db.Column(db.Integer)
    turn_rate = db.Column(db.Float)

    def __repr__(self):
        return '<Turnstile {}, group {} has turn rate {}>'.format(self.turnstile_id, self.group_id, self.turn_rate)
