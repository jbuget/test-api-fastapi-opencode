import hashlib
import uuid
from typing import Any, Dict
from src.domain.user import User
from src.domain.user_repository import UserRepository

class RegisterUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user_data: Dict[str, Any]) -> User:
        email = user_data["email"]
        password = user_data["password"]
        display_name = user_data["display_name"]

        # Check if user already exists
        existing_user = await self.user_repository.get_by_email(email)
        if existing_user:
            raise ValueError("Email already in use")

        # In a real app, we would use a proper password hashing library (e.g., passlib)
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        # Create new user
        new_user = User(
            id=str(uuid.uuid4()),
            email=email,
            password_hash=password_hash,
            display_name=display_name
        )

        # Persist user
        await self.user_repository.save(new_user)

        return new_user

class LoginUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, login_data: Dict[str, Any]) -> User:
        email = login_data["email"]
        password = login_data["password"]

        user = await self.user_repository.get_by_email(email)
        if not user:
            raise ValueError("Invalid credentials")

        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if user.password_hash != password_hash:
            raise ValueError("Invalid credentials")

        return user

