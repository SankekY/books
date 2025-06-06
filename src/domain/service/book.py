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