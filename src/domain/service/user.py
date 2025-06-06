from infrastructure.database.repository.user import UserRepository
from domain.schems.user import UserSchema, UserLogInSchema
from domain.auth.user import create_access_token, get_hash_password, verefy_password


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def create_user(self, user_data: UserSchema):
        user_data.password = get_hash_password(user_data.password)
        if await self.repository.get_user(user_data.email): 
            return None
        user = await self.repository.create_user(user_data.dict())
        return create_access_token({"email":user_data.email, "name": user_data.name})
    
    async def login_user(self, user_data: UserLogInSchema):
        user = await self.repository.get_user(user_data.email)
        if not user:
            return None
        if not verefy_password(user_data.password, user.password):
            return None      
        return create_access_token({
            "email": user.email,
            "name": user.name
        })