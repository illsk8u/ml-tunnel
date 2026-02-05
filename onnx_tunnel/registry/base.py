from typing import TypeVar, Generic, Dict, Type
from .types import RegistryTypes


ValueType = TypeVar('ValueType')


class Registry(Generic[ValueType]):
    _registry: Dict[RegistryTypes, Type[ValueType]] = {}

    @classmethod
    def register(cls, key: RegistryTypes, value: Type[ValueType]):
        cls._registry[key] = value
    
    @classmethod
    def create(cls, key: RegistryTypes, **kwargs) -> ValueType:
        if key not in cls._registry:
            raise ValueError(f"Key {key} not registered")
        return cls._registry[key](**kwargs)