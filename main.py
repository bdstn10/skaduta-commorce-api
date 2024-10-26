from fastapi import FastAPI
from database.database import init_db
from database.model import productlist

app = FastAPI()

@app.on_event('startup')
async def startup():
    init_db(app)

@app.get('/')
def read_root():
    return {"Hello": "World!!"}

@app.get('/product')
async def get_product_list():
    product_list = await productlist.all()
    
    return product_list