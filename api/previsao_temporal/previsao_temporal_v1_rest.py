from fastapi import APIRouter

from api.previsao_temporal.previsao_temporal_bo import treinar_modelo
from api.previsao_temporal.previsao_temporal_repository import get_paciente_repository, get_previsao_temporal_repository
from api.previsao_temporal.schemas.exceptions import ExceptionResponseSchema

previsao_temporal_router = APIRouter()

@previsao_temporal_router.get("",
                             response_model={},
                             response_model_exclude={},
                             responses={"400": {"model": ExceptionResponseSchema}})
async def get_paciente():
    pacientes = await get_paciente_repository()
    return pacientes

@previsao_temporal_router.get("/previsao",
                             response_model={},
                             response_model_exclude={},
                             responses={"400": {"model": ExceptionResponseSchema}})
async def get_previsao():
    pacientes = await get_previsao_temporal_repository()
    return pacientes

@previsao_temporal_router.post("/treinar",
                             response_model={},
                             response_model_exclude={},
                             responses={"400": {"model": ExceptionResponseSchema}})
async def post_treinar_previsao(qtd_dias_previsao: int = 120, 
                                qtd_dias_sazonalidade: int = 90,
                                cid: str = 'TODOS'):
    return await treinar_modelo(qtd_dias_previsao, qtd_dias_sazonalidade, cid)