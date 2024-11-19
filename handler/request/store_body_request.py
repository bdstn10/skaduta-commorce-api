from pydantic import BaseModel
from typing import Optional

class StoreBody(BaseModel):
    store_name: Optional[str]
    store_location: Optional[str]
    store_owner_id: Optional[int]