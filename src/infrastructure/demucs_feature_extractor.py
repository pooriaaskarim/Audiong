"""
Module: Demucs Feature Extractor
Location: src/infrastructure/demucs_feature_extractor.py
Uses the Demucs model to separate vocals, drums, bass, and other instruments.
"""

from demucs.apply import apply_model
from demucs.pretrained import get_model
import torchaudio

class DemucsFeatureExtractor:
    """
    Class to separate audio into vocals, drums, bass, and other instruments using Demucs.
    """

    def __init__(self):
        # Load the pre-trained Demucs model
        self.model = get_model("htdemucs")
        self.model.cpu()  # Run on CPU for simplicity

    def separate_voices(self, audio_file_path):
        """
        Separates the audio file into different components (vocals, drums, bass, other).

        Args:
            audio_file_path (str): Path to the audio file.

        Returns:
            dict: Dictionary with separated audio components (vocals, drums, bass, other).
        """
        wav, sr = torchaudio.load(audio_file_path)
        sources = apply_model(self.model, wav, split=True, shifts=1)

        return {
            'vocals': sources[0].squeeze().numpy(),
            'drums': sources[1].squeeze().numpy(),
            'bass': sources[2].squeeze().numpy(),
            'other': sources[3].squeeze().numpy(),
        }