#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth
from api.v1.auth.session_exp_auth import SessionExpAuth
from api.v1.auth.session_db_auth import SessionDBAuth
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None

auth = os.getenv('AUTH_TYPE')

if auth == 'auth':
    auth = Auth()
elif auth == 'basic_auth':
    auth = BasicAuth()
elif auth == 'session_auth':
    auth = SessionAuth()
elif auth == 'session_exp_auth':
    auth = SessionExpAuth()
elif auth == 'session_db_auth':
    auth = SessionDBAuth()


@app.before_request
def before_request():
    """checks the authorization"""
    if not auth:
        return

    if auth.require_auth(
        request.path,
        [
            '/api/v1/status/',
            '/api/v1/unauthorized/',
            '/api/v1/forbidden/',
            '/api/v1/auth_session/login/'
        ]
    ):
        if not auth.authorization_header(request) \
                and not auth.session_cookie(request):
            abort(401)

        if not auth.current_user(request):
            abort(403)

    request.current_user = auth.current_user(request)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized error handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden error handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
