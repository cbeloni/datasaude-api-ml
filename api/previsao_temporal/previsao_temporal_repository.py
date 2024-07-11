from api.previsao_temporal.queries import clean_paciente_previsao_after_data, insert_paciente_previsao, query_paciente_previsao_by_data, query_pacientes, query_paciente_previsao, update_paciente_previsao_by_data
from api.previsao_temporal.schemas.previsao_temporal_schema import PacientePrevisaoSchema
from core.config.session import session


async def get_paciente_repository():
    pacientes = (await session.execute(query_pacientes(), {"poluente": "MP10", "dt_atendimento":"2022-01-01"})).mappings().all()
    return pacientes

async def get_previsao_temporal_repository(paciente_previsao: PacientePrevisaoSchema):
    previsoes = (await session.execute(query_paciente_previsao(), paciente_previsao.model_dump())).mappings().all()
    return previsoes

async def insert_previsao_temporal_repository(paciente_previsao: PacientePrevisaoSchema):
    result = await session.execute(insert_paciente_previsao(), paciente_previsao.model_dump())
    await session.commit()
    return result

async def get_paciente_previsao_by_data_repository(paciente_previsao: PacientePrevisaoSchema):
    previsao = (await session.execute(query_paciente_previsao_by_data(), paciente_previsao.model_dump())).mappings().first()
    return previsao

async def update_paciente_previsao_by_data_repository(paciente_previsao: PacientePrevisaoSchema):
    result = await session.execute(update_paciente_previsao_by_data(), paciente_previsao.model_dump())
    await session.commit()
    return result

async def upsert_paciente_previsao_by_data_repository(paciente_previsao: PacientePrevisaoSchema):
    previsao = await get_paciente_previsao_by_data_repository(paciente_previsao)
    if previsao:
        return await update_paciente_previsao_by_data_repository(paciente_previsao)
    else:
        return await insert_previsao_temporal_repository(paciente_previsao)

async def clean_paciente_previsao_after_data_repository(paciente_previsao: PacientePrevisaoSchema):
    result = await session.execute(clean_paciente_previsao_after_data(), paciente_previsao.model_dump())
    await session.commit()
    return result