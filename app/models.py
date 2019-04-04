from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {} (id: {})>'.format(self.username, self.id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Batch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(64), index=True, unique=True)
    # status codes: 0 - test, 1 - active, 2 - inactive
    status = db.Column(db.Integer)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    insta_username = db.Column(db.String(120), index=True, unique=True)
    batch_id = db.Column(db.Integer, db.ForeignKey('batch.id'))
    labelled = db.Column(db.Boolean, default=False)

    def get_url():
        return 'https://instagram.com/{}'.format(self.insta_username)

    def __repr__(self):
        return '<Profile {} (id: {})>'.format(self.insta_username, self.id)

class Profileclass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(280))
    if_true = db.Column(db.String(64))
    if_false = db.Column(db.String(64))

    def __repr__(self):
        return '<Class {}: {} /n(id: {})>'.format(self.name, self.description, self.id)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    class_id = db.Column(db.Integer, db.ForeignKey('profileclass.id'))
    value = db.Column(db.Integer)
    session = db.Column(db.String(200))

    def __repr__(self):
        return '<User {} voted for profile {} in {} to be {}>'.format(self.user_id, self.profile_id, self.class_id, self.value)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))