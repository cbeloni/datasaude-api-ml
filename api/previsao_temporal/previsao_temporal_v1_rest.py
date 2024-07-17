from fastapi import APIRouter, HTTPException

from api.previsao_temporal.previsao_temporal_bo import treinar_modelo
from api.previsao_temporal.previsao_temporal_repository import get_paciente_repository, get_previsao_temporal_cid_repository
from api.previsao_temporal.schemas.exceptions import ExceptionResponseSchema
from api.previsao_temporal.schemas.previsao_temporal_schema import PacientePrevisaoSchema

previsao_temporal_router = APIRouter()

@previsao_temporal_router.get("",
                             response_model={},
                             response_model_exclude={},
                             responses={"400": {"model": ExceptionResponseSchema}})
async def get_pacientes():
    pacientes = await get_paciente_repository()
    return pacientes

@previsao_temporal_router.get("/previsao",
                             response_model={},
                             response_model_exclude={},
                             responses={"400": {"model": ExceptionResponseSchema}})
async def get_previsao(cid: str = 'TODOS'):
    
    paciente_previsao: PacientePrevisaoSchema = PacientePrevisaoSchema(cid=cid)
    
    pacientes = await get_previsao_temporal_cid_repository(paciente_previsao)
    return pacientes

@previsao_temporal_router.post("/treinar",
                             response_model={},
                             response_model_exclude={},
                             responses={"400": {"model": ExceptionResponseSchema}})
async def post_treinar_previsao(qtd_dias_previsao: int = 120, 
                                qtd_dias_sazonalidade: int = 90,
                                cid: str = 'TODOS'):
    try:
        return await treinar_modelo(qtd_dias_previsao, qtd_dias_sazonalidade, cid)
    except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))