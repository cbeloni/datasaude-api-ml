from datetime import date
from pydantic import BaseModel, Field
from typing import Optional


class PacientePrevisaoSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID")
    data: Optional[date] = Field(None, description="Data")
    valor_historico: Optional[int] = Field(None, description="Valor histórico")
    valor_previsao: Optional[int] = Field(None, description="Valor previsão")
    cid: Optional[str] = Field("TODOS", description="CID")
    tipo_analise: Optional[str] = Field("ATENDIMENTO", description="Tipo de Análise")

    class Config:
        orm_mode = True
        
if __name__ == '__main__':
    valores_dict = {"id":1, "data": '2022-01-01', "valor_historico": "124", "valor_previsao": "342"}
    paciente = PacientePrevisaoSchema(**valores_dict)
    print(paciente.model_dump())
    