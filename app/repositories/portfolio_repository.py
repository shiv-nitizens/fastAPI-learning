from app.database.mongodb import db


async def create_portfolio_entry(entry):
    result = await db.portfolio_entries.insert_one(
        entry.model_dump(mode="json")
    )

    return result.inserted_id

async def get_all_portfolio_entries():
    cursor = db.portfolio_entries.find({})
    entries = await cursor.to_list(length=None)

    return entries