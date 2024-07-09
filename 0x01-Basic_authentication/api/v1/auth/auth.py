#!/usr/bin/env python3
"""Authentication Module"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the given path requires authentication.
        """
        if path is None:
            return True
        if not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):
                if path == excluded_path:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from the request.
        """
        return None
