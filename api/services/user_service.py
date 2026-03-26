from bson import ObjectId
from config.database import user_collection
from utils.hash import hash_password, verify_password
from utils.jwt import create_token

async def register_user(user):
    user_dict = user.dict()
    user_dict["password"] = hash_password(user_dict["password"])
    
    result = await user_collection.insert_one(user_dict)
    return str(result.inserted_id)

async def login_user(user):
    db_user = await user_collection.find_one({"email": user.email})
    
    if not db_user:
        return None
    
    if not verify_password(user.password, db_user["password"]):
        return None

    token = create_token({"user_id": str(db_user["_id"])})
    return token