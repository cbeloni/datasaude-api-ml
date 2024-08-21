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
    
def query_paciente_previsao_historico_not_null():
    return text(""" 
                SELECT id, data, valor_historico, valor_previsao
                  FROM paciente_previsao
                 WHERE cid = :cid
                   AND tipo_analise = :tipo_analise
                   AND valor_historico is not null
                """)    

def query_paciente_cid_previsao():
    return text(""" 
                SELECT id, data, valor_historico, valor_previsao
                  FROM paciente_previsao
                 WHERE cid = :cid
                   AND tipo_analise = :tipo_analise
                """)    
    
def query_paciente_previsao_by_data():
    return text(""" 
                SELECT id, data, valor_historico, valor_previsao
                  FROM paciente_previsao
                 WHERE data = :data
                   AND cid = :cid
                   AND tipo_analise = :tipo_analise
                """)
    
def insert_paciente_previsao():
    return text(""" 
                INSERT INTO paciente_previsao (id, data, valor_historico, valor_previsao, cid, tipo_analise)
                VALUES (:id, :data, :valor_historico, :valor_previsao, :cid, :tipo_analise)
                """)
    
def update_paciente_previsao_by_data():
    return text(""" 
                UPDATE paciente_previsao
                   SET valor_historico = :valor_historico, valor_previsao = :valor_previsao
                 WHERE data = :data
                   AND cid = :cid
                   AND tipo_analise = :tipo_analise
                """)

def clean_paciente_previsao_after_data():
    return text(""" 
                UPDATE paciente_previsao
                   SET valor_previsao = null
                 WHERE data > :data
                   AND cid = :cid
                   AND tipo_analise = :tipo_analise
                """)
  
def delete_unnecessary_paciente_previsao_after_data():
    return text(""" 
                DELETE FROM paciente_previsao
                 WHERE data > :data
                   AND cid = :cid
                   AND valor_previsao is null
                   AND valor_historico is null
                   AND tipo_analise = :tipo_analise
                """)