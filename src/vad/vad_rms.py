from vad_interface import VADAdapter
import numpy as np

class RMSVADAdapter(VADAdapter):
    def __init__(self, silence_threshold):
        self.threshold = silence_threshold

    def is_silence(self, audio_chunk: np.ndarray) -> bool:
        rms = np.sqrt(np.mean(audio_chunk ** 2))
        return rms < self.threshold
