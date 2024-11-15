# Product Responses
def product_summary(id: int, product_name: str, product_price: str, sold: int, location: str, cover_link: str):
     return {
        "id": id,
        "product_name": product_name,
        "product_price": product_price,
        "sold": sold,
        "cover_link": cover_link,
        "location": location
    }

def product_detail(product_name: str, store_id: int, cover_link: str, price: str, stock: int, sold: int):
    return {
        "product_name": product_name,
        "store_id": store_id,
        "cover_link": cover_link,
        "product_price": price,
        "stock": stock,
        "sold": sold,
    }


def product_detail_with_variant(product_name: str, store_id: int, cover_link: str, variant_details: list[dict]):
    return {
        "product_name": product_name,
        "store_id": store_id,
        "cover_link": cover_link,
        "variant_details": variant_details
    }

def cart_item_response(product_id: int, product_name: str, quantity: int, cover_link: str, price: str, stock: int, variant_name: str = None, variant_option: str = None):
    return {
        "product_id": product_id,
        "product_name": product_name,
        "variant_name": variant_name,
        "variant_option": variant_option,
        "quantity": quantity,
        "cover_link": cover_link,
        "price": price,
        "stock": stock
    }