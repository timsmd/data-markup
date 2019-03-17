from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='static/dist')


@app.route('/')
# single page app handled by Vue.js
def index():
    return app.send_static_file("index.html")

@app.route('/dist/<path:path>')
# serving static files
def static_dist(path):
    return send_from_directory("static/dist", path)


if __name__ == '__main__':
    app.run()