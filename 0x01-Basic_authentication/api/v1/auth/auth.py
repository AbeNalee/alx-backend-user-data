#!/usr/bin/env python3
"""
Class Auth
"""
from flask import request

class Auth:
    def requre_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return false
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Return request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return request
        """
        return None
