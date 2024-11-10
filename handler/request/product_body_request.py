from pydantic import BaseModel
from typing import Optional

class ProductDetail(BaseModel):
    variant_name: Optional[str]
    variant_option: Optional[str]
    stock: Optional[int]
    sold: Optional[int]
    price: Optional[str]

class Product(BaseModel):
    product_name: Optional[str]
    product_cover_link: Optional[str]
    store_id: Optional[int]
    with_variant: Optional[bool]
    details: Optional[list[ProductDetail]]