from passlib.context import CryptContext
from config.settings import config
from jose import jwt, JWTError

from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException, status

from domain.schems.user import UserSchema, TokenData
from typing import Optional


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.jwt.secret_key, algorithm=config.jwt.algorithm)
    return encoded_jwt


def decode_jwt_token(token: str) -> TokenData:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try: 
        payload = jwt.decode(token=token, key=config.jwt.secret_key, algorithms=[config.jwt.algorithm])
        email: str = payload.get("sub")
        print(payload)
        if email == None:
            raise credentials_exception
        return TokenData(email=email)
    except JWTError:
        raise credentials_exception

def get_hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verefy_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

