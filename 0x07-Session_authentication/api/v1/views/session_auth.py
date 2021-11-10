#!/usr/bin/env python3
""" Module of SessionAuth views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from os import getenv
from models.user import User


@app_views.route(
    '/auth_session/login',
    methods=['POST'],
    strict_slashes=False
)
def auth_session_login() -> str:
    """ POST /auth_session/login
    Return:
      - the respons
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or email == '':
        return jsonify({"error": "email missing"}), 400
    if not password or password == '':
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    user = False

    if users and isinstance(users, list):
        for usr in users:
            if usr.is_valid_password(password):
                user = usr
                break
    else:
        return jsonify({"error": "no user found for this email"}), 404

    if not user:
        return jsonify({"error": "wrong password"}), 400

    from api.v1.app import auth

    session_id = auth.create_session(user.id)

    respon = jsonify(user.to_json())
    respon.set_cookie(getenv('SESSION_NAME'), session_id)

    return respon


@app_views.route(
    '/auth_session/logout',
    methods=['DELETE'],
    strict_slashes=False
)
def auth_session_logout() -> str:
    """ DELETE /auth_session/logout
    Return:
      - the respons
    """
    from api.v1.app import auth

    if auth.destroy_session(request):
        return jsonify({}), 200
    else:
        abort(404)
