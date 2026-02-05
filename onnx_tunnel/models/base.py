from abc import ABC, abstractmethod
from typing import TypeVar, Generic

InputModelDataType = TypeVar('InputModelDataType')
OutputModelDataType = TypeVar('OutputModelDataType')


class BaseModel(Generic[InputModelDataType, OutputModelDataType], ABC):
    
    def __init__(self, model_path: str):
        self.model_path = model_path


    @abstractmethod
    def predict(self, data: InputModelDataType) -> OutputModelDataType:
        pass

    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(model_path='{self.model_path}'"
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__} at '{self.model_path}'"