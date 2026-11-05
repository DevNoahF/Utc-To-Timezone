

class UserRepository(UserRepositoryInterface):
    def __init__(
        self,
        session
    ):
        self.session = session
        
    