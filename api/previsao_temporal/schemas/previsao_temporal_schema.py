from datetime import date
from pydantic import BaseModel, Field


class PacientePrevisaoSchema(BaseModel):
    id: int = Field(..., description="ID")
    data: str = Field(..., description="Data")
    valor_historico: date = Field(..., description="Valor histórico")
    valor_previsao: date = Field(..., description="Valor previsão")

    class Config:
        orm_mode = True