from fastapi import APIRouter, HTTPException, status
from app.schemas.auth import RegisterRequest, LoginRequest
from app.services.auth_service import register_user,login_user
from app.security.auth import get_current_user
from fastapi import Depends

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED
)
async def register(request: RegisterRequest):

    try:
        user = await register_user(
            request.email,
            request.username,
            request.password
        )
        return {
            "id": user.id,
            "email": user.email,
            "username": user.username
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )

@router.post("/login")
async def login(request: LoginRequest):
    try:
        return await login_user(
            request.email,
            request.password
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )

@router.get("/me")
async def get_me(user = Depends(get_current_user)):
    return user