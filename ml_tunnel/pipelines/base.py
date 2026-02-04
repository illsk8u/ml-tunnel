from typing import TypeVar, Generic

InputType = TypeVar('InputType')
ModelDataType = TypeVar('ModelDataType')
OutputType = TypeVar('OutputType')


class BasePipeline(Generic[InputType, ModelDataType, OutputType]):

    @staticmethod
    def preprocess(data: InputType) -> ModelDataType:
        raise NotImplementedError("Preprocess not implemented.")

    @staticmethod
    def postprocess(data: ModelDataType) -> OutputType:
        raise NotImplementedError("Postprocess not implemented.")