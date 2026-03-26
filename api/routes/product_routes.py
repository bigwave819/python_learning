from fastapi import APIRouter, Depends, HTTPException
from schemas.product_schema import ProductCreate
from services.product_service import create_product, get_products, delete_product
from utils.dependecies import get_current_user

router = APIRouter()

# CREATE (AUTH REQUIRED)
@router.post("/products")
async def create(product: ProductCreate, user=Depends(get_current_user)):
    product_id = await create_product(product, user["user_id"])
    return {"message": "Product created", "id": product_id}

# VIEW (PUBLIC)
@router.get("/products")
async def read_all():
    return await get_products()

# DELETE (OWNER ONLY)
@router.delete("/products/{product_id}")
async def delete(product_id: str, user=Depends(get_current_user)):
    result = await delete_product(product_id, user["user_id"])
    
    if result is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if result == "unauthorized":
        raise HTTPException(status_code=403, detail="Not allowed")
    
    return {"message": "Product deleted"}