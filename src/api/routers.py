from fastapi import APIRouter
from api.enpoints import book
from api.enpoints import user

router = APIRouter()
router.include_router(book.router)
router.include_router(user.router)