#!/usr/bin/env python3
"""This module contains the BasicAuth class
"""

from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth class"""
    def extract_base64_authorization_header(
        self,
        authorization_header: str
    ) -> str:
        """returns the Base64 part of the Authorization header
        for a Basic Authentication:
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if len(authorization_header) > 6:
            if 'Basic ' in authorization_header[0:6]:
                return authorization_header[6:]

        return None

    def decode_base64_authorization_header(
        self,
        base64_authorization_header: str
    ) -> str:
        """returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None

        value = base64_authorization_header
        try:
            return base64.b64decode(value).decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str
    ) -> (str, str):
        """returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        else:
            splited = decoded_base64_authorization_header.split(':', 1)
            return splited[0], splited[1]

    def user_object_from_credentials(
        self,
        user_email: str,
        user_pwd: str
    ) -> TypeVar('User'):
        """returns the User instance based on his email and password.
        """
        if user_email is None or user_pwd is None:
            return None
        if type(user_email) is not str or type(user_pwd) is not str:
            return None

        try:
            users = User().search({'email': user_email})
        except Exception:
            return None

        if users and isinstance(users, list):
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request:
        """
        auth_header = self.authorization_header(request)
        b64_auth = self.extract_base64_authorization_header(auth_header)
        auth_value = self.decode_base64_authorization_header(b64_auth)
        user_email, user_pwd = self.extract_user_credentials(auth_value)
        user = self.user_object_from_credentials(user_email, user_pwd)

        return user
