from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    product_name: Optional[str]
    product_stock: Optional[int]
    product_sold: Optional[int]
    product_price: Optional[str]
    product_img_link: Optional[str]