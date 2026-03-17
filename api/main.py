from fastapi import FastAPI, HTTPException
from schema import User
from database import user_collection
from bson import ObjectId

app = FastAPI()

@app.get('/')
def read_root():
    return{ "message": "Hello world with fastapi" }


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"]
    }

# CREATE

@app.post("/users")
async def create_user(user: User):
    newUser = await user_collection.insert_one(user.dict())    
    created_user = await user_collection.find_one({"_id": newUser.inserted_id})
    return user_helper(created_user)

# GET ALL USERS
@app.get('/users')
async def get_users():
    users = []
    async for user in  user_collection.find():
        users.append(user_helper(user))
    return users

# GET ONE USER
@app.get("/users/{user_id}")
async def get_user(user_id: str):
    user = await user_collection.find_one({ "_id": ObjectId(user_id) })
    if user:
        return user_helper(user)
    raise HTTPException(status_code=404, detail=" User not found ")

# UPDATE THE USER
@app.put("/users/{user_id}")
async def update_user(user_id: str, user: User):
    updated = await user_collection.update_one(
        { "_id": ObjectId(user_id) },
        { "$set": user.dict() }
    )

    if updated.modified_count == 1:
        updated_user = await user_collection.find_one({ "_id": objectId(user_id) })
        return user_helper(updated_user)

    raise HTTPException(status_code = 404, detail = "User not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    deleted = await user_collection.delete_one({ "_id": ObjectId(user_id) })
    if deleted.deleted_count == 1:
        return { "message": "User deleted" }

    raise HTTPException(status_code = 404, detail = "User not found")