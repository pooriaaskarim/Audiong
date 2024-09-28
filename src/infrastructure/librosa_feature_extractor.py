"""
Module: Librosa Feature Extractor with K-S Algorithm and Genre-Specific Profiles
Location: src/infrastructure/librosa_feature_extractor.py
Implements the extraction of musical features using the Librosa library,
with key estimation handled by the Krumhansl-Schmuckler algorithm.
"""

import librosa
from src.infrastructure.ks_key_finder import KrumhanslSchmucklerKeyFinder
from src.entities.audio_file import AudioFile  # Corrected Import


class LibrosaFeatureExtractor:
    """
    Implements the extraction of musical features (tempo, key, pitch, rhythm) from audio files using Librosa,
    and uses the Krumhansl-Schmuckler algorithm for key estimation.

    Methods:
        extract: Extracts musical features from the given audio file.
    """

    def __init__(self, genre='general'):
        self.ks_key_finder = KrumhanslSchmucklerKeyFinder(genre)

    def extract(self, audio_file: AudioFile):
        """
        Extracts musical features such as tempo, key, pitch, and rhythm from the audio file.

        Args:
            audio_file (AudioFile): The audio file to extract features from.

        Returns:
            dict: A dictionary containing tempo, key, pitch, and rhythm data.
        """
        # Load the audio file using librosa
        y, sr = librosa.load(audio_file.file_path, sr=audio_file.sample_rate)

        # Extract tempo
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

        # Use K-S algorithm to estimate key
        key = self.ks_key_finder.estimate_key(audio_file.file_path, audio_file.sample_rate)

        # Extract pitch using librosa's pitch detection
        pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)
        pitch_values = self._get_pitch_values(pitches, magnitudes)

        # Rhythm (time of beats)
        rhythm = librosa.frames_to_time(beat_frames, sr=sr)

        return {
            "tempo": tempo,
            "key": key,
            "pitch": pitch_values[:10],  # Return first 10 pitch values for simplicity
            "rhythm": rhythm.tolist()  # Convert numpy array to list
        }

    def _get_pitch_values(self, pitches, magnitudes):
        """
        Extract pitch values from the pitch tracking matrix.

        Args:
            pitches (np.ndarray): Pitch array.
            magnitudes (np.ndarray): Magnitude array corresponding to the pitches.

        Returns:
            list: Filtered pitch values (in Hz).
        """
        pitch_values = []
        for t in range(pitches.shape[1]):
            index = magnitudes[:, t].argmax()
            pitch = pitches[index, t]
            if pitch > 0:
                pitch_values.append(pitch)
        return pitch_values