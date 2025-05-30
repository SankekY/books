from infrastructure.database.repository.base import BaseRepository
from domain.models.book import Book

class BookRepository(BaseRepository[Book]):

    async def create_item(self, book_data: dict) -> Book:
        book = Book(**book_data)
        self.session.add(book)
        await self.session.commit()
        await self.session.refresh(book)
        return book
