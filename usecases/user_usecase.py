from fastapi import Response

from dtos.request.user_request_dto import UserRequest, UserUpdateRequest
from dtos.response.user_response_dto import UserResponse
from gateways.user_repository_interface import UserRepositoryInterface
from infrastructure.database.models.user import User
from middleware.convert_to_user_timezone_middleware import ConvertToUserTimezoneMiddleware


class UserUsecase:
    def __init__(
        self,
        repository: UserRepositoryInterface,
        convert_timezone: ConvertToUserTimezoneMiddleware | None = None,
    ):
        self.repository = repository
        self.convert_timezone = convert_timezone or ConvertToUserTimezoneMiddleware()


    def __map_user_to_response(self, user: User, timezone: str) -> UserResponse:
        return UserResponse(
            id=user.Id,
            name=user.Name,
            email=user.Email,
            timezone=user.Timezone,
            created_at=self.convert_timezone.convert_to_user_timezone(user.CreatedAt, timezone),
            updated_at=(
                self.convert_timezone.convert_to_user_timezone(user.UpdatedAt, timezone)
                if user.UpdatedAt
                else None
            ),
        )

    async def create_user(self, body: UserRequest) -> UserResponse:
        await self.repository.create_user(body)
        return Response(status_code=201)


    async def update_user(self, body: UserUpdateRequest) -> UserResponse:
        user_existing = await self.repository.get_user_by_id(body.id)
        if user_existing is None:
            return Response(status_code=404)
        user = await self.repository.update_user(user_existing, body)
        if not user:
            return Response(status_code=500)

        return Response(status_code=200)



    async def get_all_users(self, timezone: str) -> list[UserResponse]:
        users = await self.repository.get_all_users()
        if not users:
            return Response(status_code=204)

        return [self.__map_user_to_response(user, timezone) for user in users]


    async def get_user_by_id(self, user_id: int, timezone: str) -> UserResponse:
        user = await self.repository.get_user_by_id(user_id)
        if user is None:
            return Response(status_code=404)

        return self.__map_user_to_response(user, timezone)
