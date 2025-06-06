from passlib.context import CryptContext
from config.settings import config
from jose import jwt
from datetime import datetime, timedelta, timezone
from config.settings import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    return jwt.encode(
        to_encode,
        algorithm=config.jwt.algorithm,
        key=config.jwt.secret_key
    )

def get_hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verefy_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)