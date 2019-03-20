from flask import jsonify, send_from_directory
from app import app

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
            'version': '0.0.1'
        })

if __name__ == '__main__':
    app.run()