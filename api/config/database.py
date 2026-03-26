from motor.motor_asyncio import AsyncIOMotorClient

MongoDbUrl = "mongodb://127.0.0.1:27017/expense"

client = AsyncIOMotorClient(MongoDbUrl)
database = client["fast_crud"]

user_collection = database["none"]
product_collection = database["products"]