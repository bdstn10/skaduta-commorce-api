from fastapi import APIRouter
from fastapi.responses import JSONResponse
from database.model import productlist, productvariants,storelist
from handler.request.product_body_request import Product
from handler.response.response import product_summary

router = APIRouter(prefix='/products',tags=['Store-Products'])

@router.get('/get-list')
async def get_prod_list():
    products = await productlist.all()

    return products

@router.get('/get-prod-sum')
async def get_product_summary():
    products = await productlist.all()
    response = []
    
    for product in products:
        id = product.product_id
        product_variant = await productvariants.filter(product_id=id).first()
        product_store = await product.store_id.first()
        response.append(product_summary(product.name, product_variant.price, product_variant.sold, product_store.location, product.img_link))
        
    
    return response

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