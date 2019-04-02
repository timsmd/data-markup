from flask import jsonify, send_from_directory, request
from flask_login import current_user, login_user, logout_user
from app import app, db
from app.models import User

inputForm = 'server'

@app.route('/api/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		if current_user.is_authenticated:
			return redirect('/')
		post_data = request.get_json()
		user = User.query.filter_by(username=post_data['username']).first()
		if (user is None) or (not user.check_password(post_data['password'])):
			return jsonify({
				'logged_in': False,
				'username': post_data['username']
			})
		login_user(user)
		return jsonify({
			'logged_in': True,
			'username': post_data['username']
		})
	return(jsonify({
		'info': 'login url'
	}))

@app.route('/api/logout')
def logout():
	try:
		logout_user()
	except:
		return jsonify({
			'logged_out': False
		})
	else:
		return jsonify({
			'logged_out': True
		})

@app.route('/api/signup', methods=['POST', 'GET'])
def sign_up():
	if request.method == 'POST':
		post_data = request.get_json()
		if User.query.filter_by(username=post_data['username']).first() is not None:
			return jsonify({
				'info': 'username taken',
				'signed_up': False
			})
		new_user = User(username=post_data['username'])
		new_user.set_password(post_data['password'])
		db.session.add(new_user)
		db.session.commit()
		return(jsonify({
			'username': new_user.username,
			'signed_up': True
		}))
	return(jsonify({
		'info': 'sign up url'
	}))

if __name__ == '__main__':
	app.run()