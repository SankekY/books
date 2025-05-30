from domain.schems.book import BookCreate, BookResponse
from infrastructure.database.repository.book import BookRepository

class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    async def create_book(self, book_data: BookCreate) -> BookResponse:
        item = await self.repository.create_item(book_data.model_dump())
        return BookResponse.model_validate(item)