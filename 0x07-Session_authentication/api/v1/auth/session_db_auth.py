#!/usr/bin/env python3
"""This module contains the SessionExpAuth class
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth Class"""
    def create_session(self, user_id=None):
        """creates and stores new instance of UserSession
        and returns the Session ID
        """
        if not user_id:
            return

        session_id = super().create_session(user_id)
        if not session_id:
            return

        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        UserSession.save_to_file()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """returns the User ID by requesting UserSession
        in the database based on session_id
        """
        if not session_id:
            return None

        UserSession.load_from_file()

        users = UserSession.search({'session_id': session_id})

        session_duration = timedelta(seconds=self.session_duration)

        for user in users:
            if user.created_at + session_duration < datetime.now():
                return None
            return user.user_id

    def destroy_session(self, request=None):
        """destroys the UserSession
        based on the Session ID from the request cookie
        """
        if not request:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False

        users = UserSession.search({'session_id': session_id})
        for user in users:
            user.remove()
            UserSession.save_to_file()
            return True

        return False
