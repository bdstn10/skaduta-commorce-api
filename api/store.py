from fastapi import APIRouter
from database.model import storelist
from handler.request.store_body_request import StoreBody

router = APIRouter(prefix='/stores',tags=['Stores'])

@router.get('/get-store-list')
async def get_store_list():
    response = await storelist.filter().limit(50)

    return response

@router.post('/create-store')
async def create_store(store: StoreBody):
    created_store = await storelist.create(name=store.store_name, location=store.store_location, owner_id=store.store_owner_id)
    
    return {
        "status": 'ok',
        "created_store": {
            "name": created_store.location,
            "location": created_store.name
        }
    }