from fastapi import APIRouter, status, Depends, HTTPException
from domain.schems.user import UserSchema, UserLogInSchema
from api.deps import get_user_service
from domain.service.user import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Users"]
)

@router.post(
    "/register",
    status_code=status.HTTP_200_OK,
)
async def register_user(
    user_data: UserSchema,
    service: UserService = Depends(get_user_service)
) -> dict:
    token = await service.create_user(user_data)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с таким Email уже есть!"
        )
    return {
        "access":True,
        "token":token
    }


@router.post(
    "/login",
    status_code=status.HTTP_200_OK
)
async def login_user(
    user_data: UserLogInSchema,
    service: UserService = Depends(get_user_service)
) -> dict:
    token = await service.login_user(user_data)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Не верный логин или пороль!"
        )
    return {
        "access": True, 
        "token": token
    }