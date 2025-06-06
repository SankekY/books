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


@router.get(
    "/",
    response_model=list[BookResponse],
    status_code=status.HTTP_200_OK   
)
async def get_books(
    offset: int = 0,
    limit: int = 25,
    service: BookService = Depends(get_book_service)
) -> list[BookResponse]:
    return await service.get_books(offset, limit) 

@router.get(
    "/{book_id}",
    response_model=BookResponse,
    status_code=status.HTTP_200_OK
)
async def get_book(
    book_id: int,
    service: BookService = Depends(get_book_service)
) -> BookResponse:
    return await service.get_book(book_id)