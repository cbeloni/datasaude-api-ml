from fastapi import FastAPI
from api import router
from typing import List
from fastapi.middleware import Middleware
from core.config.SQLAlchemyMiddleware import SQLAlchemyMiddleware
from fastapi.middleware.cors import CORSMiddleware

def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)

def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(SQLAlchemyMiddleware),
    ]
    return middleware

app = FastAPI(middleware=make_middleware())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

init_routers(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)