from fastapi import APIRouter

router = APIRouter(prefix="/catalog", tags=["catalog"])

@router.get("/")
async def index():
    return "Hello Catalog"