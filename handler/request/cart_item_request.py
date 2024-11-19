from pydantic import BaseModel
from typing import Optional,Union

class CartItem(BaseModel):
    cart_id: Optional[int]
    product_id: Optional[int]
    variant_name: Optional[str]
    variant_option: Optional[str]
    quantity: Optional[int]