from fastapi import APIRouter
from fastapi.responses import JSONResponse
from database.model import productlist, productdetails,storelist
from handler.request.product_body_request import Product,ProductDetail
from handler.response.response import product_summary,product_detail,product_detail_with_variant

router = APIRouter(prefix='/products',tags=['Products'])

@router.get('/product-list')
async def get_prod_list():
    products = await productlist.all()

    return products

@router.get('/get-product-detail')
async def get_product_detail(product_id: int):
    product = await productlist.filter(product_id=product_id).first()
    response = []
    
    if product.with_variant is True:
        product_details = await productdetails().filter(product_id=product)
        variant_details = []
        
        for pd in product_details:
            variant_details.append({
                "variant_name": pd.variant_name,
                "variant_option": pd.variant_option,
                "stock": pd.stock,
                "sold": pd.sold,
                "price": pd.price
            })    
            
        response = product_detail_with_variant(product.name, product.store_id_id, product.cover_link, variant_details=variant_details)    
    else:
        pass
    
    return response
    
    # for product in products:
    #     id = product.product_id
    #     product_variant = await productvariants.filter(product_id=id).first()
    #     product_store = await product.store_id.first()
    #     response.append(product_summary(product.name, product_variant.price, product_variant.sold, product_store.location, product.img_link))
        
    # return response

@router.post('/add-product')
async def add_prod(product: Product):
    product_details = product.details
    store_id = await storelist.filter(store_id=product.store_id).first()
    
    new_product = await productlist.create(name=product.product_name,cover_link=product.product_cover_link,with_variant=product.with_variant, store_id=store_id)
    
    if not product.with_variant:
        product_details = product_details[0]
        await productdetails.create(stock=product_details.stock, price=product_details.price, sold=product_details.sold, product_id=new_product)
    else:
        for detail in product_details:
            await productdetails.create(variant_name=detail.variant_name, variant_option=detail.variant_option,stock=detail.stock, price=detail.price, sold=detail.sold, product_id=new_product)
    
    return JSONResponse({
        "status": "ok",
        "added_product": {
            "product_name": product.product_name,
            "product_cover_link": product.product_cover_link,
            "with_variant": product.with_variant,
        }
    }, status_code=201)  