import jwt
import datetime
import json
from flask import jsonify


def get_token(user, secret):
    token = jwt.encode({'public_id': user.id, 'exp': datetime.datetime.utcnow(
    ) + datetime.timedelta(minutes=30)}, secret, algorithm='HS512')
    return token


def user_token_json(user, token):
    return json.dumps({"result": user.json, "token": token})
