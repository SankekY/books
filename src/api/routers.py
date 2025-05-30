from fastapi import APIRouter
from api.enpoints import book

router = APIRouter()
router.include_router(book.router)