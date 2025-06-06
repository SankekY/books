from pydantic import BaseModel, Field, EmailStr, validator
import re

class UserSchema(BaseModel):
    name: str = Field(..., description="User Name")
    email: EmailStr = Field(..., description="Youre Email")
    password: str = Field(..., min_length=5, max_length=50, description="Password lenght: min 5, max 50")
    phone_number: str = Field(..., description="+7 000 000 00 00")

    @validator("phone_number")
    @classmethod
    def validate_phone_number(cls, value: str) -> str:
        if not re.match(r'^\+\d{5,15}$', value):
            raise ValueError("Номер телефона должен начинаться с "+" и содержать от 5 до 15 цифр")
        return value

    class Config:
        from_attributes = True

class UserLogInSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True