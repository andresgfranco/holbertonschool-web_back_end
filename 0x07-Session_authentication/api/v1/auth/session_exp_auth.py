#!/usr/bin/env python3
"""This module contains the SessionExpAuth class
"""

from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """SessionExpAuth Class"""
    def __init__(self):
        """SessionExpAuth Constructor"""
        s_d = 0

        try:
            s_d = int(getenv('SESSION_DURATION'))
        except TypeError:
            s_d = 0

        self.session_duration = s_d

    def create_session(self, user_id=None):
        """creates a Session ID for an user_id"""
        session_id = super().create_session(user_id)

        if not session_id:
            return None

        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """returns a User ID based on a Session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None

        session_dict = self.user_id_by_session_id.get(session_id)
        if not session_dict:
            return None

        if self.session_duration <= 0:
            return session_dict.get('user_id')

        created_at = session_dict.get('created_at')
        if not created_at:
            return None

        session_duration = timedelta(seconds=self.session_duration)
        if created_at + session_duration < datetime.now():
            return None

        return session_dict.get('user_id')
