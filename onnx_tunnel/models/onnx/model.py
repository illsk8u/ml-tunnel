from typing import cast, List
from ..base import BaseModel

from .io import ONNXModelInput, ONNXModelOutput

import numpy as np
import onnxruntime as ort


class ONNXModel(BaseModel[ONNXModelInput, ONNXModelOutput]):
    def __init__(self, model_path: str):
        super().__init__(model_path)
        self.session = ort.InferenceSession(model_path)

    def predict(self, data: ONNXModelInput) -> ONNXModelOutput:
        outputs = cast(List[np.ndarray], self.session.run(data["output_names"], data["inputs"]))
        return {
            "outputs": outputs
        }