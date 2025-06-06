from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse

async def auth_middleware(request: Request, call_next):
    if not request.headers.get("Authorization"):
        return JSONResponse(
        content={
            "error": "Unauthorized"
        },
        status_code=status.HTTP_401_UNAUTHORIZED
        )
    try:
        token = request.headers.get("Authorization")
        pass
    except HTTPException as e:
        return JSONResponse(
            content={
                "error": e.detail
            },
            status_code=e.status_code
        )
