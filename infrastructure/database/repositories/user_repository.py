from dtos.request.user_request_dto import UserRequest,UserUpdateRequest
from infrastructure.database.models.user import User
from gateways.user_repository_interface import UserRepositoryInterface
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
class UserRepository(UserRepositoryInterface):
    def __init__(
        self,
        session: AsyncSession
    ):
        self.session = session


    async def create_user(self, body: UserRequest):
        async with self.session as session:
            try:
                user = User(
                        Name=body.name,
                        Email=body.email,
                        Timezone=body.timezone,
                    )
                session.add(user)
                await session.commit()
                return user
            except Exception as e:
                await session.rollback()
                print(e, "create_user - UserRepository")


    async def update_user(self, user: User, body: UserUpdateRequest):
        async with self.session as session:
            try:
                user.Name = body.name
                user.Email = body.email
                user.Timezone = body.timezone

                session.add(user)
                await session.commit()
                await session.refresh(user)
                return user
            except Exception as e:
                await session.rollback()
                print(e, "update_user - UserRepository")

    async def get_user_by_id(self, user_id: int):
        async with self.session as session:
            try:
                result = await session.execute(
                    select(
                        User
                    ).where(
                        User.Id == user_id
                    )
                )
                return result.scalar_one_or_none()
            
            except Exception as e:
                await session.rollback()
                print(e, "get_user_by_id - UserRepository")
                raise

    async def get_all_users(self):
        async with self.session as session:
            try:
                users = await session.execute(select(User))
                return users.scalars().all()
            
            except Exception as e:
                print(e, "get_all_users - UserRepository")
