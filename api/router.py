from fastapi import APIRouter
from api.product import router as prod_router
from api.account import router as acc_router
from api.store import router as store_router

router = APIRouter(prefix='/api')

router.include_router(prod_router)
router.include_router(acc_router)
router.include_router(store_router)