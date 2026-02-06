from typing import Any, List, TypedDict

import numpy as np


class ONNXModelInput(TypedDict):
    inputs: List[np.ndarray]
    outputs: List[np.ndarray]

ONNXModelOutput = Any