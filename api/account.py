from fastapi import APIRouter
from database.model import userlist

router = APIRouter(prefix='/accounts',tags=['Accounts'])

@router.get('/user-list')
async def get_user_list():
    return await userlist.all()