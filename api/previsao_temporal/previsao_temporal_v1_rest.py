from fastapi import APIRouter

from api.previsao_temporal.previsao_temporal_repository import obtem_paciente_service

previsao_temporal_router = APIRouter()

@previsao_temporal_router.get("")
async def get_previsao(response_model={}):
    return await obtem_paciente_service()
