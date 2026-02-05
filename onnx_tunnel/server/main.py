from fastapi import FastAPI

from ..registry import RegistryTypes

def create_app(args) -> FastAPI:
    from .routers import index_router 
    from .lifespan import app_lifespan


    app = FastAPI(lifespan=app_lifespan)


    app.include_router(index_router)


    app.state.model_path = args.model
    app.state.provider = RegistryTypes(args.provider)

    return app