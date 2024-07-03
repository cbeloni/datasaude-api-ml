
from fastapi import APIRouter


temporal_router = APIRouter()

@temporal_router.get("")
def get_previsao():
    return {"message": "Endpoint de previsão"}
