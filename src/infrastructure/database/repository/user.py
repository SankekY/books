from infrastructure.database.repository.base import BaseRepository
from sqlalchemy import select, delete, update
from domain.models.user import User

class UserRepository(BaseRepository[User]):
    
    async def create_user(self, user_data: dict) -> User:
        user = User(**user_data)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    async def get_user(self, email) -> User:
        query = select(User).where(User.email == email)
        result = await self.session.execute(query)
        return result.scalar_one_or_none() 