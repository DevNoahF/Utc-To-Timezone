from fastapi import status
from fastapi import APIRouter
from dtos.request import UserRequest, UserUpdateRequest

class UserController:
    app = APIRouter()
    
    def __init__(
        self,
    ):
        self,
    pass

    @app.post("/users") 
    def create_user(self, user: UserRequest):
        pass
    
    @app.put("/users")
    def update_user(self, user: UserUpdateRequest):
        pass
    
    @app.get("/users")
    def get_users(self):
        pass
    
    @app.get("/users/{user_id}")
    def get_user(self, user_id: int):
        pass
