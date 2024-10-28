from fastapi import APIRouter
from api.product_display import router as prod_router

router = APIRouter(prefix='/api')

router.include_router(prod_router)