from contextlib import asynccontextmanager

from fastapi import FastAPI

from ..registry import Registry
from ..models import BaseModel
from ..pipelines import BasePipeline

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    model_registry = Registry[BaseModel]()
    pipeline_registry = Registry[BasePipeline]()

    app.state.model_registry = model_registry
    app.state.pipeline_registry = pipeline_registry

    app.state.model = model_registry.create(app.state.provider, model_path=app.state.model_path)
    app.state.pipeline = pipeline_registry.create(app.state.provider)
    yield