from abc import ABC, abstractmethod
import numpy as np

class VADAdapter(ABC):
    @abstractmethod
    def is_silence(self, audio_chunk: np.ndarray) -> bool:
        pass
