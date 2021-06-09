from flask import request, jsonify, current_app
from recipefinder.models import User
from functools import wraps
import jwt


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return jsonify({'message': "Token is missing!"}), 401
        try:
            data = jwt.decode(
                token, current_app.config['SECRET_KEY'], algorithms=['HS512'])
            current_user = User.query.get(data['public_id'])
        except:
            return jsonify({'message': 'Token is invalid'}), 401
        (current_user.name)
        return f(current_user, *args, **kwargs)
    return decorated
