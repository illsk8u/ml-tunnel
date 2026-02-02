from fastapi import FastAPI

from .routers import index_router 


app = FastAPI()


app.include_router(index_router)