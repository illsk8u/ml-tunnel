from ..base import BaseModel

from .io import ONNXModelInput, ONNXModelOutput

import onnxruntime as ort


class ONNXModel(BaseModel[ONNXModelInput, ONNXModelOutput]):
    def __init__(self, model_path: str):
        super().__init__(model_path)
        self.session = ort.InferenceSession(model_path)

    def predict(self, data: ONNXModelInput) -> ONNXModelOutput:
        return self.session.run(data["outputs"], data["inputs"])