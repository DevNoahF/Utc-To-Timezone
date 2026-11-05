from pydantic import BaseModel, Field

class UserRequest(BaseModel):
    Name: str
    Email: str
    Timezone: str

class UserUpdateRequest(BaseModel):
    Id: int
    Name: str
    Email: str
    Timezone: str
