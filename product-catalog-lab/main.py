# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(
    title="Product Catalog API",
    description="A simple API for managinga product catalog"
)

# Define Pydantic model for Product
class Product(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None

# Mock in-memory database
products_db = [
    Product(id=1, name="Laptop", price=999.99, description="High-end gaminglaptop"),
    Product(id=2, name="Wireless Mouse", price=29.99, description="Ergonomicwireless mouse"),
    Product(id=3, name="Keyboard", price=59.99),
]

@app.get("/products", response_model=List[Product])
async def list_products():
    """Retrieve a list of all products in the catalog."""
    return products_db

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """Retrieve a specific product by its ID."""
    for product in products_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
