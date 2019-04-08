import sys
from app import app, db
from app.models import Batch, Profile

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
        db.session.commit()
    except:
        print('error commiting changes to database')
    else:
        print('{} profiles added to database'.format(counter))

# use by typing python batch-upload.py filename, batch_number, status(see models for status codes)
if __name__ == '__main__':
    module_name, filename, batch_number, status = sys.argv
    new_batch = create_batch(batch_number, status)

    if new_batch is not None:
        load_profiles(filename, new_batch)