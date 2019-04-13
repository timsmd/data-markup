from flask import jsonify
from app import app, db

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({
        'info': 'something went wrong'
    }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'info': 'page not found'
        }), 400