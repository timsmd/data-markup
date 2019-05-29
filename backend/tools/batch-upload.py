import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from app import app, db
from app.models import Batch, Profile


def remove_existing(filename):
    with open(filename) as f:
        add_usernames = [each.strip() for each in f.readlines()]
    existing = [each.insta_username for each in Profile.query.all()]

    new_usernames = [x for x in add_usernames if x not in existing]

    with open(filename, 'w') as f:
        for user in new_usernames:
            f.write("{}\n".format(user))
        

def create_batch(number, status):
    new_batch = Batch(number=number, status=status)
    try:
        db.session.add(new_batch)
        db.session.commit()
    except:
        return None
    else:
        return Batch.query.get(new_batch.id)

def load_profiles(filename, batch):
    counter = 0
    with open(filename) as f:
        for line in f:
            counter += 1
            line = line.rstrip()
            new_profile = Profile(insta_username=line, batch_id=batch.id)
            db.session.add(new_profile)
    try:
        print('lol')
        db.session.commit()
    except Exception as er:
        print(er)
        print('error commiting changes to database')
    else:
        print('{} profiles added to database'.format(counter))

# use by typing python batch-upload.py filename, batch_number, status(see models for status codes)
if __name__ == '__main__':
    module_name, filename, batch_number, status = sys.argv
    remove_existing(filename)
    new_batch = create_batch(batch_number, status)

    if new_batch is not None:
        load_profiles(filename, new_batch)
