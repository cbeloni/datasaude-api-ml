from fastapi import APIRouter
from api.previsao_temporal.previsao_temporal_v1_rest import previsao_temporal_router

router = APIRouter()

router.include_router(previsao_temporal_router, prefix="/api/temporal", tags=["Previsão"])

__all__ = ["router"]