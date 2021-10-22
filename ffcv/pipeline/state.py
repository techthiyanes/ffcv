
from dataclasses import dataclass
from typing import Literal, Tuple

import torch as ch
import numpy as np

from .stage import Stage, ALL_STAGES

@dataclass
class State:
    stage: ALL_STAGES
    jit_mode: bool
    device: ch.device
    shape: Tuple[int, ...]
    dtype: np.dtype
    
    # Assess the validity of a pipeline stage
    def __post_init__(self):
        if self.jit_mode and self.device != ch.device('cpu'):
            raise AssertionError("Can't be in JIT mode and on the GPU")
        
        if self.stage == Stage.INDIVIDUAL and not self.jit_mode:
            raise AssertionError("Individual processing has to be in JIT mode")
        