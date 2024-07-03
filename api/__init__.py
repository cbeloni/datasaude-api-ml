from fastapi import APIRouter
from api.previsao.temporal_v1 import temporal_router
router = APIRouter()

router.include_router(temporal_router, prefix="/api/temporal", tags=["Previsão"])

__all__ = ["router"]