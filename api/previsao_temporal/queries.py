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
    
def query_paciente_previsao():
    return text(""" 
                SELECT id, data, valor_historico, valor_previsao
                  FROM paciente_previsao
                """)    
    
def insert_paciente_previsao():
    return text(""" 
                INSERT INTO paciente_previsao (id, data, valor_historico, valor_previsao)
                VALUES (:id, :data, :valor_historico, :valor_previsao)
                """)