#!/usr/bin/env python3
"""A module containing password hashing for users"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Hashes a password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def _generate_uuid() -> str:
    """Generates a new UUID string"""
    string = uuid.uuid4()
    return str(string)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initializes the class"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registers a user"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password=password)
            return self._db.add_user(email, hashed_password.decode('utf-8'))

    def valid_login(self, email: str, password: str) -> bool:
        """Validates a user login using details"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode('utf-8'), user.hashed_password.encode('utf-8'))
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """"""
        session_id = _generate_uuid()