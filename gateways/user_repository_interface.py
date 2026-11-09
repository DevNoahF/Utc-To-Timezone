from __future__ import annotations

from abc import ABC, abstractmethod

from dtos.request.user_request_dto import UserRequest, UserUpdateRequest
from infrastructure.database.models.user import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    async def create_user(self, body: UserRequest) -> User:
        ...

    @abstractmethod
    async def update_user(self, user: User, body: UserUpdateRequest) -> User:
        ...

    @abstractmethod
    async def get_all_users(self) -> list[User]:
        ...

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> User | None:
        ...
