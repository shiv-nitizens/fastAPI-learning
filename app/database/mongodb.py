from pymongo import AsyncMongoClient
from bson.codec_options import CodecOptions
from bson.binary import UuidRepresentation
from app.config import settings

client = AsyncMongoClient(
    settings.mongodb_url,
    uuidRepresentation="standard"
)

db = client[settings.mongodb_database]