from api.previsao_temporal.queries import query_pacientes, query_paciente_previsao
from core.config.session import session


async def get_paciente_repository():
    pacientes = (await session.execute(query_pacientes(), {"poluente": "MP10", "dt_atendimento":"2022-01-01"})).mappings().all()
    return pacientes

async def get_previsao_temporal_repository():
    previsoes = (await session.execute(query_paciente_previsao())).mappings().all()
    return previsoes
