from fastapi import APIRouter
from app.views.base_view import success_response
router=APIRouter(tags=["health"])
@router.get('/health')
async def health(): return success_response("API healthy")
