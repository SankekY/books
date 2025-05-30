from pydantic import BaseModel, Field

class BookCreate(BaseModel): 
    title: str = Field(max_length=30)
    author: str = Field(max_length=30)
    description: str | None
    year: int 
    copies: int = Field(default=1)

class BookResponse(BookCreate):
    id: int 
    class Config:
        from_attributes = True  # Для совместимости с SQLAlchemy (ex-Orm mode)