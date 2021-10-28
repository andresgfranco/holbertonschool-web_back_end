#!/usr/bin/env python3
"""This module contains the hash_password function"""


import bcrypt


def hash_password(password: str) -> bytes:
    """expects one string argument name password and
        returns a salted, hashed password, which is a byte string.
    """
    salt = bcrypt.gensalt()

    return bcrypt.hashpw(password.encode(), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """checks for a valid hash_password and returns a boolean"""
    if bcrypt.checkpw(password.encode(), hashed_password):
        return True
    else:
        return False
