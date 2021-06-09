from flask import Blueprint, jsonify, request, current_app
from recipefinder import db
from recipefinder.models import User, UserSchema
from werkzeug.security import generate_password_hash, check_password_hash
from recipefinder.users.utils import get_token, user_token_json
import jwt
import datetime

users = Blueprint('users', __name__)
user_schema = UserSchema()

# id
# email
# name
# password
# liked_recipes
# disliked_recipes
# recipes
# saved_recipes


@users.post('/user/signup')
def user_create():
    data = request.json
    email = data['email']
    name = f'{data["firstName"]} {data["lastName"]}'
    password = generate_password_hash(data['password'], method='sha256')
    try:
        new_user = User(email, name, password)
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return jsonify({'message': 'Error occured creating new user'}), 400
    db.session.flush()
    token = get_token(new_user, current_app.config['SECRET_KEY'])
    return user_token_json(user_schema.jsonify(new_user), token), 200


@users.post('/user/login')
def user_login():
    data = request.json
    email = data['email']
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'message': "User with the given email does not exist"}), 404
    if not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'verification failed'}), 401
    token = get_token(user, current_app.config['SECRET_KEY'])
    return user_token_json(user_schema.jsonify(user), token), 200
