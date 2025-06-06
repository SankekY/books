from infrastructure.database.repository.base import BaseRepository
from sqlalchemy import select
from domain.models.book import Book

class BookRepository(BaseRepository[Book]):

    async def create_item(self, book_data: dict) -> Book:
        book = Book(**book_data)
        self.session.add(book)
        await self.session.commit()
        await self.session.refresh(book)
        return book

    async def get_books(self, offset, limit) -> list[Book]:
        qery = select(
            Book
        ).offset(offset).limit(limit)
        books = await self.session.execute(qery)
        return books.scalars().all()