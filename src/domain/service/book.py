from domain.schems.book import BookCreate, BookResponse
from infrastructure.database.repository.book import BookRepository

class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    async def create_book(self, book_data: BookCreate) -> BookResponse:
        item = await self.repository.create_item(book_data.model_dump())
        return BookResponse.model_validate(item)

    async def get_books(self, offset: int, limit: int) -> list[BookResponse]:
        books = await self.repository.get_books(offset, limit)
        book_list = []
        for book in books:
            book_list.append(
                BookResponse.from_orm(book)
            )
        return book_list
    
    async def get_book(self,id: int) -> BookResponse:
        book = await self.repository.get_book(id)
        return BookResponse.from_orm(book)

    async def delete_book(self, book_id: int) -> BookResponse:
        return await self.repository.delete_book(book_id)

    async def update_book(self, book_data: BookCreate, book_id: int) -> BookResponse:
        return await self.repository.update_book(
            book_data=book_data.dict(),
            book_id=book_id
        )