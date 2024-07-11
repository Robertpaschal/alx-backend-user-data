#!/usr/bin/env python3
"""A new flask view that handles all routes for session authenticato"""
from api.v1.views import app_views
from models.user import User
from flask import jsonify, request
from api.v1 import auth
import os


@app_views.route(
        '/auth_session/login',
        methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    POST /api/v1/auth_session/login

    Return
    - retrieves email and password
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or len(email) == 0:
        return jsonify({"error": "email missing"}), 400
    if not password or len(password) == 0:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)

    response = jsonify(user.to_json())
    session_name = os.getenv('SESSION_NAME')
    response.set_cookie(session_name, session_id)

    return response
