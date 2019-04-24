import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from app import app, db
from app.models import Vote, Profile

votes = db.session.query(Profile, Vote).filter(Vote.value != -1).filter(Vote.profile_id == Profile.id).all()

votes_cast = "votes.txt"
usernames = "voted_profiles.txt"

with open(votes_cast, 'w') as v_f:
    with open(usernames, 'w') as f:
        for each in votes:
            v_f.write("{}, {}\n".format(each[0].insta_username, each[1].value))
            f.write("{}\n".format(each[0].insta_username))