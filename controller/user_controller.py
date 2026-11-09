from typing import Annotated

from fastapi import APIRouter, Depends, Header as FastAPIHeader, status
from sqlalchemy.ext.asyncio import AsyncSession

from dtos.request.user_request_dto import UserRequest, UserUpdateRequest
from dtos.response.user_response_dto import UserResponse
from dtos.request.header_request_dto import TypeTimezone
from infrastructure.database.config import get_session
from infrastructure.database.repositories.user_repository import UserRepository
from usecases.user_usecase import UserUsecase

router = APIRouter(prefix="/users")


def get_usecase(session: Annotated[AsyncSession, Depends(get_session)]) -> UserUsecase:
    return UserUsecase(UserRepository(session))


UserService = Annotated[UserUsecase, Depends(get_usecase)]


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(body: UserRequest, usecase: UserService):
    return await usecase.create_user(body)


@router.put("", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def update_user(body: UserUpdateRequest, usecase: UserService):
    return await usecase.update_user(body)


@router.get("", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
async def get_users(
    timezone: Annotated[TypeTimezone, FastAPIHeader(alias="Timezone")],
    usecase: UserService,
):
    return await usecase.get_all_users(timezone.value)


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    timezone: Annotated[TypeTimezone, FastAPIHeader(alias="Timezone")],
    usecase: UserService,
):
    return await usecase.get_user_by_id(user_id, timezone.value)
