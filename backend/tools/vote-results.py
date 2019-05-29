import sys
import os.path
import csv

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from app import app, db
from app.models import Vote, Profile

votes = db.session.query(Profile, Vote).filter(Vote.profile_id == Profile.id)

votes_file = "classes.csv"
usernames_file = "voted_profiles.txt"

usernames = set()

usernames.update([each[0].insta_username for each in votes.all()])

# write file with usernames for further [rofile crawling
# with open(usernames_file, 'w') as f:
#     for uname in usernames:
#         f.write("{}\n".format(uname))

# write csv file with votes

cl_dict = dict([
    (4, 'bot'),
    (3, 'corpotate'),
    (2, 'commercial'),
    (1, 'individual')
])


with open(votes_file, 'w', newline='') as csvfile:
    fieldnames = [
        'username',
        'bot',
        'commercial',
        'individual',
        'corpotate'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for each in usernames:
        votes_dict = {}
        for vote in votes.filter(Profile.insta_username == each).all():
            votes_dict[cl_dict[vote[1].class_id]] = vote[1].value
        writer.writerow({
            'username': each,
            'bot': votes_dict['bot'],
            'commercial': votes_dict['commercial'],
            'individual': votes_dict['individual'],
            'corpotate': votes_dict['corpotate']
        })





