from core.config.standalone_session import standalone_session
from core.config.session import session
from sqlalchemy import text


def query_pacientes():
    return text("""   
           SELECT p.cd_atendimento, p.nm_paciente, pi.id, pi.data, pc.longitude, pc.latitude, pc.x, pc.y, pi.indice_interpolado as indice, pi.poluente
          FROM paciente p, paciente_coordenadas pc, paciente_interpolacao pi
         WHERE p.id = pc.id_paciente
           AND pc.id = pi.id_coordenada
           AND DT_ATENDIMENTO =  :dt_atendimento
           AND pi.poluente = :poluente
           AND pc.validado = 1
           AND pc.latitude is not null;
    """)

async def obtem_paciente_service():
    pacientes = (await session.execute(query_pacientes(), {"poluente": "MP10", "dt_atendimento":"2022-01-01"})).all()
    return pacientes
