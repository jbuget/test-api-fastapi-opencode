from typing import Protocol, runtime_checkable
from .user import User

@runtime_checkable
class UserRepository(Protocol):
    async def save(self, user: User) -> None:
        ...

    async def get_by_email(self, email: str) -> User | None:
        ...

    async def get_by_id(self, user_id: str) -> User | None:
        ...
