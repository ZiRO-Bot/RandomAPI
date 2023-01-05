from fastapi import APIRouter
from internal.google import Google


google = Google()
router = APIRouter()

@router.get("/search")
async def search(q: str | None = None):
    if not q:
        return {}
    return await google.search(q)
