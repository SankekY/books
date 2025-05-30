from fastapi import APIRouter, Depends, status
from domain.schems.book import BookCreate, BookResponse
from domain.service.book import BookService
from api.deps import get_book_service

router = APIRouter(prefix="/books", tags=["Books"])

@router.post(
    "/",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_book(
    book_data: BookCreate,
    service: BookService = Depends(get_book_service)
) -> BookResponse:
    return await service.create_book(book_data)