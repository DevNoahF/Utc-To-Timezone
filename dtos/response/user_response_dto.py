from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    timezone: str
    created_at: str
    updated_at: str | None = None
