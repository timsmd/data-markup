from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {} (id: {})>'.format(self.username, self.id)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    insta_username = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<Profile {} (id: {})>'.format(self.insta_username, self.id)

class Profileclass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(280))

    def __repr__(self):
        return '<Class {}: {} /n(id: {})>'.format(self.name, self.description, self.id)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    class_id = db.Column(db.Integer, db.ForeignKey('profileclass.id'))

    def __repr__(self):
        return '<User {} voted for profile {} to be {}>'.format(self.user_id, self.profile_id, self.class_id)
