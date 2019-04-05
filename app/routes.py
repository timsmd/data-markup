from flask import jsonify, send_from_directory, request
from flask_login import current_user, login_user, logout_user
from app import app, db
from app.models import User, Profile, Profileclass, Vote, Batch
from datetime import datetime

@app.route('/api/vote', methods=['POST', 'GET'])
def cast_vote():
	if request.method == 'POST':
		if current_user.is_authenticated:
			# session required?
			post_data = request.get_json()
			profile = post_data['current_profile']
			votes = post_data['current_votes']
			for each in votes:
				voted_class = each['class']
				voted_value = each['value']
				new_vote = Vote(user_id=current_user.id, profile_id=profile, class_id=voted_class, value=voted_value)

@app.route('/api/classes')
# TODO refactor, looks bad
def get_classes():
	classes = Profileclass.query.all()
	response = {
		'classes': []
	}
	for each in classes:
		current_class = {}
		current_class['id'] = each.id
		current_class['name'] = each.class_name
		current_class['if_true'] = each.if_true
		current_class['if_false'] = each.if_false
		response['classes'].append(current_class)
	
	return(jsonify(response))

@app.route('/api/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		if current_user.is_authenticated:
			return jsonify({
				'logged_in': False,
				'username': post_data['username']
			})
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

	