from fastapi import APIRouter
from database.model import storelist

router = APIRouter(prefix='/stores',tags=['Stores'])

@router.get('/get-store-list')
async def get_store_list():
    response = await storelist.filter().limit(50)

    return response