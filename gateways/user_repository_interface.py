from dtos.request import UserRequest, UserUpdateRequest

class UserRepositoryInterface():
    def __init__(
        self,
    ):
        self,
    pass

    def create_user(self, body:UserRequest):
        pass
    
    def update_user(self, body:UserUpdateRequest):
        pass
    
    def get_users(self):
        pass
    
    def get_user_by_id(self, user_id: int):
        pass