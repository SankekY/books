from domain.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"
    name: Mapped[str]
    email: Mapped[str] = mapped_column(primary_key=True)
    password: Mapped[str] 
    phone_number: Mapped[str] 
