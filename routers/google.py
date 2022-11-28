from utils import SingletonAiohttp
from fastapi import APIRouter
from api.google import Google


google = Google(session=SingletonAiohttp.get_aiohttp_client())
router = APIRouter()

@router.get("/search")
async def search(q: str | None = None):
    if not q:
        return {}
    return await google.search(q)
