from fastapi import APIRouter


router = APIRouter(prefix=__name__)


@router.get("/")
async def index():
    return {"message": "Hello World"}