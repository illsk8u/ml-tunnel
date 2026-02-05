from typing import TypeVar, Generic

InputType = TypeVar('InputType')
InputModelDataType = TypeVar('InputModelDataType')
OutputModelDataType = TypeVar('OutputModelDataType')
OutputType = TypeVar('OutputType')


class BasePipeline(Generic[InputType, InputModelDataType, OutputModelDataType, OutputType]):

    @staticmethod
    def preprocess(data: InputType) -> InputModelDataType:
        raise NotImplementedError("Preprocess not implemented.")

    @staticmethod
    def postprocess(data: OutputModelDataType) -> OutputType:
        raise NotImplementedError("Postprocess not implemented.")