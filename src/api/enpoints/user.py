from fastapi import APIRouter, status, Depends, HTTPException, Request
from domain.schems.user import UserSchema, UserLogInSchema, Token, TokenData, UserSchemaResponse
from api.deps import get_user_service
from domain.service.user import UserService
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from domain.auth.user import  create_access_token, decode_jwt_token, get_current_user
from config.settings import config
from datetime import timedelta


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")

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
) -> Token:
    token = await service.create_user(user_data)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с таким Email уже есть!"
        )
    return Token(
        access_token=token,
        token_type="bearer"
    )


@router.post(
    "/login",
    status_code=status.HTTP_200_OK
)
async def login_user(
    user_data: UserLogInSchema,
    service: UserService = Depends(get_user_service)
) -> Token:
    token = await service.login_user(user_data)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Не верный логин или пороль!"
        )
    return Token(
        access_token=token,
        token_type="Bearer"
    )

@router.post(
    "/token",
    response_model=Token,
    status_code=status.HTTP_200_OK
)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: UserService = Depends(get_user_service)

) -> Token:
    user = await service.chek_user(form_data.username, form_data.password) 
    if user == None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(days=config.jwt.expire_day)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="Bearer")


@router.get(
    "/users/me/",
    response_model=UserSchemaResponse
)
async def read_users_me(
    user_data: TokenData = Depends(get_current_user),
    service: UserService = Depends(get_user_service)
) -> UserSchemaResponse:

    return await service.get_user(email=user_data.email)