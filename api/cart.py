from fastapi import APIRouter
from database.model import cartitem,productdetails
from handler.response.response import cart_item_response

router = APIRouter(prefix='/cart',tags=['Cart'])

@router.get('/get-cart-items')
async def get_cart_items(cart_id: int):
    items = await cartitem.filter(cart_id=cart_id).order_by("created_at")
    response = []
    
    for item in items:
        product = await item.product.first()
        details: productdetails
        cart_item = {}
        
        if item.variant_name is not None:
            details = await productdetails.get(product_id=product, variant_option=item.variant_option)
            cart_item = cart_item_response(item.product_id, product.name, item.quantity, product.cover_link, details.price, details.stock, item.variant_name, item.variant_option)
        else:
            details = await productdetails.get(product_id=product)
            cart_item = cart_item_response(item.product_id, product.name, item.quantity, product.cover_link, details.price, details.stock)
        
        response.append(cart_item)
        
    
    return response