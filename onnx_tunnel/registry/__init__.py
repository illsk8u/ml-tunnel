from .base import Registry, RegistryTypes

from ..models import BaseModel
from ..pipelines import BasePipeline

MODEL_REGISTRY = Registry[BaseModel]()
PIPELINE_REGISTRY = Registry[BasePipeline]()