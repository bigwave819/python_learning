from fastapi import FastAPI
from routes import user_routes
from routes import product_routes

app = FastAPI()

app.include_router(user_routes.router, prefix="/api")
app.include_router(product_routes.router, prefix="/api")