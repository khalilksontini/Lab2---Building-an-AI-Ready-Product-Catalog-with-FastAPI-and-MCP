# mcp_server.py
import sys
from pathlib import Path
import asyncio
from contextlib import asynccontextmanager

# Ensure the project root is in the Python path
sys.path.append(str(Path(__file__).parent))

from fastmcp import FastMCP
from main import products_db, Product
from typing import List

# Initialize FastMCP
mcp = FastMCP(
    name="Product Catalog MCP Server",
)

@mcp.tool()
def list_products() -> List[dict]:
    """List all available products with their ID, name, price, and description."""
    return [product.model_dump() for product in products_db]

@mcp.tool()
def get_product(product_id: int) -> dict:
    """Retrieve details of a specific product by its ID.
    Args:
        product_id: The unique identifier of the product
    """
    for product in products_db:
        if product.id == product_id:
            return product.model_dump()
    return {"error": "Product not found"}

if __name__ == "__main__":
    mcp.run()
