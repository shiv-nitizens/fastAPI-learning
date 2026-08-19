from datetime import datetime, timezone
from uuid import uuid4
from pwdlib import PasswordHash
from app.models.user import User
from app.repositories.user_repository import get_user_by_email,create_user
from app.security.jwt import create_access_token

password_hash = PasswordHash.recommended()

async def register_user(email, username, password):
    existing_user = await get_user_by_email(email)
    if existing_user:
        raise ValueError("Email already registered")

    hashed_password = password_hash.hash(password)

    user = User(
        id=uuid4(),
        email=email,
        username=username,
        password_hash=hashed_password,
        created_at=datetime.now(timezone.utc)
    )

    await create_user(user)

    return user

async def login_user(email, password):
    user = await get_user_by_email(email)
    if not user:
        raise ValueError("Invalid email or password")
    if not password_hash.verify(password, user["password_hash"]):
        raise ValueError("Invalid email or password")
    access_token = create_access_token(user["id"])
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }