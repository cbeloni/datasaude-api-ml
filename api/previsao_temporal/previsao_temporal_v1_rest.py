from fastapi import APIRouter

from api.previsao_temporal.previsao_temporal_repository import obtem_paciente_service
from api.previsao_temporal.schemas.exceptions import ExceptionResponseSchema

previsao_temporal_router = APIRouter()

@previsao_temporal_router.get("",
                             response_model={},
                             response_model_exclude={},
                             responses={"400": {"model": ExceptionResponseSchema}})
async def get_previsao():
    pacientes = await obtem_paciente_service()
    return pacientes
