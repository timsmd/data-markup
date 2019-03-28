from flask import jsonify, send_from_directory, request
from flask_login import current_user, login_user, logout_user
from app import app, db
from app.models import User

inputForm = 'server'

@app.route('/api/properties')
def properties():
	return jsonify({
			'version': '0.0.1',
			'inputForm': inputForm
		})

@app.route('/api', methods=['POST', 'GET'])
def postApi():
	if request.method == 'POST':
		post_data = request.get_json()
		inputForm = post_data['data']
		return jsonify({
				'recieved': 'OK',
				'data': post_data['data']
			})
	return jsonify({
		'recieved': 'NO'
	})

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

@app.route('/api/logout', methods=['POST', 'GET'])
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
		new_user = User(username=post_data['username'])
		new_user.set_password(post_data['password'])
		db.session.add(new_user)
		db.session.commit()
		return(jsonify({
			'username': new_user.username,
			'signed_up': True
		}))

if __name__ == '__main__':
	app.run()