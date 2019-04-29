from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import func
from app import db, login

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

    def get_url(self):
        return 'https://instagram.com/{}'.format(self.insta_username)

    def get_iframe_desktop(self):
        return 'https://www.yooying.com/{}'.format(self.insta_username)

    def get_iframe_mobile(self):
        return 'https://web.stagram.com/{}'.format(self.insta_username)

    def get_dict(self):
        return({
            'id': self.id,
            'insta_username': self.insta_username,
            'batch_id': self.batch_id,
            'labelled': self.labelled,
            'url': self.get_url(),
            'iframe_desktop': self.get_iframe_desktop(),
            'iframe_mobile': self.get_iframe_mobile()
        })

    def __repr__(self):
        return '<Profile {} (id: {})>'.format(self.insta_username, self.id)

    def check_labelled(self):
        votes_per_class_counts = db.session.query(Profileclass, func.count(Vote.id)).\
        select_from(Vote).filter(Vote.value !=-1).filter(Vote.class_id == Profileclass.id).\
        join(Profile).filter(Profile.id == self.id).group_by(Profileclass.id).all()
        
        if (len(votes_per_class_counts) <= 0):
            return False

        for current_class, votes_count in votes_per_class_counts:
            if (votes_count < 3):
                return False

        current_profile = Profile.query.filter_by(id=self.id).first()
        current_profile.labelled = True
        db.session.commit()
        return True

class Profileclass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(280))
    if_true = db.Column(db.String(64))
    if_false = db.Column(db.String(64))

    def get_dict(self):
        return({
            'id': self.id,
            'name': self.class_name,
            'description': self.description,
            'if_true': self.if_true,
            'if_false': self.if_false
        })

    def __repr__(self):
        return '<Class {}: {} \n(id: {})>'.format(self.class_name, self.description, self.id)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    class_id = db.Column(db.Integer, db.ForeignKey('profileclass.id'))
    value = db.Column(db.Integer)
    session = db.Column(db.String(200))
    __table_args__ = (
        db.UniqueConstraint('user_id', 'profile_id', 'class_id', name='user_class_profile_uc'),
        db.UniqueConstraint('session', 'profile_id', 'class_id', name='session_class_profile_uc')
    )

    def __repr__(self):
        return '<User {}(s: {}) voted for profile {} in {} to be {}>'.format(self.user_id, self.session, self.profile_id, self.class_id, self.value)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))