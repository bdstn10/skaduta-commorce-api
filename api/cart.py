from fastapi import APIRouter
from database.model import cartitem,productdetails
from handler.response.response import cart_item_response
from handler.request.cart_item_request import CartItem

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
            cart_item = cart_item_response(item.id, item.product_id, product.name, item.quantity, product.cover_link, details.price, details.stock, item.variant_name, item.variant_option)
        else:
            details = await productdetails.get(product_id=product)
            cart_item = cart_item_response(item.id, item.product_id, product.name, item.quantity, product.cover_link, details.price, details.stock)
        
        response.append(cart_item)
        
    
    return response

@router.post('/add-cart-item')
async def add_cart_item(cart_item: CartItem):
    await cartitem.create(cart_id=cart_item.cart_id, product_id=cart_item.product_id, quantity=cart_item.quantity, variant_name=cart_item.variant_name, variant_option=cart_item.variant_option)
    
    return True

@router.put('/modify-cart-quantity')
async def modify_cart_quantity(cartitem_id: int, modifier: int):
    cart_item = await cartitem.filter(id=cartitem_id).first()
    item_quantity = cart_item.quantity
    item_details = await productdetails.get(product_id_id=cart_item.product_id, variant_option=cart_item.variant_option)
    
    # increase or decrease quantity
    # 1 = increase & 2 decrease
    if modifier == 1 and item_quantity < item_details.stock:
        cart_item.quantity += 1
    elif modifier == 2 and item_quantity > 1:
        cart_item.quantity -= 1
        
    await cart_item.save()
        
    return True

@router.delete('/delete-cart-item')
async def delete_cart_item(cartitem_id: int):
    await cartitem.filter(id=cartitem_id).delete()
    
    return True