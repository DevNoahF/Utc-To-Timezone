from pydantic import BaseModel
from typing import Optional

class UserResponse(BaseModel):
    Id: int
    Name: str
    Email: str
    Timezone: str
    CreatedAt: str
    UpdatedAt: Optional[str] = None