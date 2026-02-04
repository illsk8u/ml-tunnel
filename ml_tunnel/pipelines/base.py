from typing import TypeVar, Generic, Any

InputType = TypeVar('InputType')
OutputType = TypeVar('OutputType')


class BasePipeline(Generic[InputType, OutputType]):

    @staticmethod
    def preprocess(data: Any) -> InputType:
        raise NotImplementedError("Preprocess not implemented.")

    @staticmethod
    def postprocess(data: Any) -> OutputType:
        raise NotImplementedError("Postprocess not implemented.")