# Product Responses
def product_summary(product_title: str, product_price: str, sold: int, location: str, img_link: str):
     return {
        "product_title": product_title,
        "product_price": product_price,
        "sold": sold,
        "img_link": img_link,
        "location": location
    }