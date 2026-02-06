from typing import List, TypedDict

import numpy as np


class ONNXModelInput(TypedDict):
    inputs: List[np.ndarray]
    output_names: List[str]


class ONNXModelOutput(TypedDict):
    outputs: List[np.ndarray]