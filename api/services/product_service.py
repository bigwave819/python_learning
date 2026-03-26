from config.database import product_collection
from bson import ObjectId

# CREATE
async def create_product(product, user_id):
    product_dict = product.dict()
    product_dict["owner_id"] = user_id
    
    result = await product_collection.insert_one(product_dict)
    return str(result.inserted_id)

# GET ALL (PUBLIC)
async def get_products():
    products = []
    async for product in product_collection.find():
        product["_id"] = str(product["_id"])
        products.append(product)
    return products

# DELETE (ONLY OWNER)
async def delete_product(product_id, user_id):
    product = await product_collection.find_one({"_id": ObjectId(product_id)})
    
    if not product:
        return None
    
    # CHECK OWNER
    if product["owner_id"] != user_id:
        return "unauthorized"
    
    await product_collection.delete_one({"_id": ObjectId(product_id)})
    return "deleted"