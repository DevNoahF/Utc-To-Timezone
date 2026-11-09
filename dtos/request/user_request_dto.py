from pydantic import BaseModel


class UserRequest(BaseModel):
    name: str
    email: str
    timezone: str


class UserUpdateRequest(UserRequest):
    id: int
