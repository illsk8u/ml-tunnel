from abc import ABC, abstractmethod
from typing import TypeVar, Generic

InputType = TypeVar('InputType')
OutputType = TypeVar('OutputType')


class BaseModel(Generic[InputType, OutputType], ABC):
    
    def __init__(self, model_path: str):
        self.model_path = model_path


    @abstractmethod
    def predict(self, data: InputType) -> OutputType:
        pass

    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(model_path='{self.model_path}'"
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__} at '{self.model_path}'"