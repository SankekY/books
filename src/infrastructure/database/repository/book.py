from infrastructure.database.repository.base import BaseRepository
from sqlalchemy import select, delete, update
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
    
    async def get_book(self, id: int) -> Book:
        stmt = select(Book).where(Book.id == id)
        book = await self.session.execute(stmt)
        return book.scalar_one()

    async def delete_book(self, book_id: int):
        query = delete(Book).where(Book.id == book_id)
        result =  await self.session.execute(query)
        await self.session.commit()
        return result.scalar_one()

    async def update_book(self, book_data: dict, book_id: int):
        book = Book(**book_data)
        exists_query = select(exists().where(Book.id == book_id))
        result = await self.session.execute(exists_query)
        if not result.scalar():
            raise ValueError(f"Book with ID: {book_id} not found!")
        
        update_query = update(Book).where(Book.id == book_id).values(**book_data)
        await self.session.execute(update_query)
        await self.session.commit()

        querty = select(Book).where(Book.id == id)
        result = await self.session.execute(querty)
        return result.scalar_one()