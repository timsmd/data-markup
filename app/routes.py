from flask import jsonify, send_from_directory, request
from app import app
import inspect, pprint

inputForm = 'server'

@app.route('/')
# single page app handled by Vue.js
def index():
	return app.send_static_file("index.html")

@app.route('/dist/<path:path>')
# serving static files
def static_dist(path):
	return send_from_directory("static/dist", path)

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

if __name__ == '__main__':
	app.run()