from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.database.session import get_session
from domain.service.book import BookService
from infrastructure.database.repository.book import BookRepository
from domain.models.book import Book

async def get_book_service(
    session: AsyncSession = Depends(get_session)
) -> BookService:
    repo = BookRepository(model=Book, session=session)
    return BookService(repository=repo)