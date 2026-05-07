"""Exceptions raised by the JWTManager.
"""


class InvalidSignature(Exception):
    """Couldn't validate the token signature.
    """


class ExpiredToken(Exception):
    """Token has expired.
    """


class InvalidToken(Exception):
    """Token is invalid.
    """
