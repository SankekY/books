from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from domain.auth.user import decode_jwt_to
ken

async def jwt_middleware(request: Request, call_next):
    # Пропускаем определенные пути
    if request.url.path in ["/docs", "/openapi.json", "/token", "/login", "/register"]:
        return await call_next(request)
    
    try:
        token = request.headers.get("Authorization").split(" ")[1]
        payload = decode_jwt_token(token)
        request.state.user = payload  # Добавляем данные пользователя в запрос
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    
    response = await call_next(request)
    return response