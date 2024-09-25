"""
Module: Librosa Feature Extractor
Location: src/infrastructure/librosa_feature_extractor.py
Implements the extraction of musical features using librosa.
"""

import librosa
import numpy as np
from src.entities.audio_file import AudioFile

class LibrosaFeatureExtractor:
    """
    Implements the extraction of musical features (tempo, key, pitch, rhythm) from audio files using librosa.

    Methods:
        extract: Extracts musical features from the given audio file.
    """

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

        # Extract tempo and beat frames
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

        # Estimate key (based on chroma features)
        chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
        key = self._estimate_key(chroma)

        # Extract pitch (using librosa's pitch detection)
        pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)
        pitch_values = self._get_pitch_values(pitches, magnitudes)

        # Convert beat frames to time (rhythm)
        rhythm = librosa.frames_to_time(beat_frames, sr=sr)

        return {
            "tempo": tempo,
            "key": key,
            "pitch": pitch_values[:10],  # Return first 10 pitch values for simplicity
            "rhythm": rhythm.tolist()    # Convert numpy array to list
        }

    def _estimate_key(self, chroma):
        """
        Estimate the musical key from chroma features.

        Args:
            chroma (np.ndarray): Chroma feature matrix.

        Returns:
            str: Estimated key as a string.
        """
        chroma_means = chroma.mean(axis=1)
        key_index = np.argmax(chroma_means)
        # Mapping key index to musical keys (e.g., C major, D major, etc.)
        keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        return f"{keys[key_index]} major"

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