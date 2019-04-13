from app import app, db
from app.models import User, Profile, Profileclass, Vote, Batch

@app.shell_context_processor
def make_shell_context():
	return {
		'db': db,
		'User': User,
		'Profile': Profile,
		'Profileclass': Profileclass,
		'Vote': Vote,
        'Batch': Batch
	}