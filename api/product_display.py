from fastapi import APIRouter
from database.model import productlist

router = APIRouter(prefix='/products',tags=['Store-Products'])

@router.get('/get-list')
async def get_prod_list():
    products = await productlist.all()

    return products