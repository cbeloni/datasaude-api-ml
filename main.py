from fastapi import FastAPI
from api import router

def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)

app = FastAPI()
init_routers(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)