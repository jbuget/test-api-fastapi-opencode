import uuid
import re

class User:
    def __init__(self, id: str, email: str, password_hash: str, display_name: str):
        self.id = id
        self.email = self._validate_email(email)
        self.password_hash = password_hash
        self.display_name = display_name

    def _validate_email(self, email: str) -> str:
        email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format")
        return email
