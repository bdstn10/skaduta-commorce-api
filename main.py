from fastapi import FastAPI
from database.database import init_db
from api.router import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.on_event('startup')
async def startup():
    init_db(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router=router)