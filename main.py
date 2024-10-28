from fastapi import FastAPI
from database.database import init_db
from api.router import router

app = FastAPI()

@app.on_event('startup')
async def startup():
    init_db(app)

app.include_router(router=router)