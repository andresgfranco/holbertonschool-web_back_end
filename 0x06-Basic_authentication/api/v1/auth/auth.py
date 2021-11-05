#!/usr/bin/env python3
"""This module contains the Auth class
"""

from flask import request
from typing import List, TypeVar
import re


class Auth():
    """This class is the template for all authentication system in this API
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """validates if path require auth"""
        slashed_path = path
        if path is None or excluded_paths is None:
            return True

        if path[-1] != '/':
            slashed_path = path + '/'

        for i in excluded_paths:
            if len(i) > 0:
                if i[-1] != '/':
                    i += '/'

                i = i.replace('*', '.*')
                i = i.replace('/', '\\/')

                if slashed_path in re.findall(i, slashed_path):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """return the value of the header request Authorization
        """
        if request is None:
            return None

        if request.headers.get('Authorization'):
            return request.headers.get('Authorization')

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """unused method"""
        return None
