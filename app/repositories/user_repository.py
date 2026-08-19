from app.database.mongodb import db
from uuid import UUID

async def get_user_by_email(email):
    return await db.users.find_one({
        "email": email
    })

async def create_user(user):
    document = {
        "id": user.id,
        "email": user.email,
        "username": user.username,
        "password_hash": user.password_hash,
        "created_at": user.created_at
    }

    await db.users.insert_one(document)

    return user

async def get_user_by_id(user_id):
    document = await db.users.find_one({
        "id": UUID(user_id)
    })

    if document:
        document.pop("_id", None)

    return document