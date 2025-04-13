from vad_interface import VADAdapter
import numpy as np
from silero import VAD as SileroVADCore  # Import the VAD helper class

class SileroVADAdapter(VADAdapter):
    def __init__(self, device='cpu'):
        self.vad = SileroVADCore(device=device)

    def is_silence(self, audio_chunk: np.ndarray) -> bool:
        """
        Returns True if silence is detected (i.e., speech probability < 0.5).
        """
        if audio_chunk.ndim == 1:
            audio_chunk = audio_chunk[np.newaxis, :]
        speech_probs = self.vad(audio_chunk)
        return float(speech_probs[0]) < 0.5
