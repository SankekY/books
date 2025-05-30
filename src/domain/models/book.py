from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from domain.models.base import Base

class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(25), nullable=False)
    author: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    year: Mapped[int] = mapped_column(nullable=False)
    copies: Mapped[int] = mapped_column(default=1)
