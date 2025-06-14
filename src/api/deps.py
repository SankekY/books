from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.database.session import get_session
from domain.service.book import BookService
from infrastructure.database.repository.book import BookRepository
from domain.models.book import Book
from domain.schems.user import TokenData
from domain.auth.user import decode_jwt_token

from domain.models.user import User
from domain.service.user import UserService
from infrastructure.database.repository.user import UserRepository

async def get_book_service(
    session: AsyncSession = Depends(get_session)
) -> BookService:
    repo = BookRepository(model=Book, session=session)
    return BookService(repository=repo)


async def get_user_service(
    session: AsyncSession = Depends(get_session)
) -> UserService:
    repo = UserRepository(model=User, session=session)
    return UserService(repository=repo)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")
async def get_current_user(
    token: str = Depends(oauth2_scheme)
) -> TokenData:
    return decode_jwt_token(token=token)
