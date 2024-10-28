from fastapi import APIRouter
from fastapi.responses import JSONResponse
from database.model import productlist
from handler.request.product_body_request import Product

router = APIRouter(prefix='/products',tags=['Store-Products'])

@router.get('/get-list')
async def get_prod_list():
    products = await productlist.all()

    return products

@router.post('/add-product')
async def add_prod(product: Product):
    new_product = productlist(name=product.product_name, stock=product.product_stock, sold=product.product_sold, price=product.product_price, img_link=product.product_img_link)
    
    await new_product.save()
    
    return JSONResponse({
        "status": "ok",
        "added_product": {
            "product_name": product.product_name,
            "product_stock": product.product_stock,
            "product_sold": product.product_sold,
            "product_price": product.product_price,
            "product_img_link": product.product_img_link
        }
    }, status_code=201)