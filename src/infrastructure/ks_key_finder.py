"""
Module: Krumhansl-Schmuckler Key Finding Algorithm with Genre-Specific Profiles
Location: src/infrastructure/ks_key_finder.py
Implements the Krumhansl-Schmuckler key-finding algorithm with genre-specific profiles for better accuracy.
"""

import numpy as np
import librosa
from src.infrastructure.genre_profile import GeneralProfile, ClassicalProfile, JazzProfile, PopProfile


class KrumhanslSchmucklerKeyFinder:
    """
    Implements the Krumhansl-Schmuckler key-finding algorithm with genre-specific profiles.
    """

    def __init__(self, genre='general'):
        """
        Initializes the Krumhansl-Schmuckler algorithm with the appropriate genre-specific profiles.
        """
        if genre == 'classical':
            self.genre_profile = ClassicalProfile()
        elif genre == 'jazz':
            self.genre_profile = JazzProfile()
        elif genre == 'pop':
            self.genre_profile = PopProfile()
        else:
            self.genre_profile = GeneralProfile()  # Default to general

    def estimate_key(self, audio_file_path, sample_rate=44100):
        """
        Estimates the musical key of the audio file using the Krumhansl-Schmuckler algorithm.

        Args:
            audio_file_path (str): Path to the audio file.
            sample_rate (int): The sample rate for the audio file.

        Returns:
            str: The estimated key as a string (e.g., "C major", "A minor").
        """
        # Load the audio file and extract chroma features
        y, sr = librosa.load(audio_file_path, sr=sample_rate)
        chroma = librosa.feature.chroma_cqt(y=y, sr=sr)

        # Compute the average chroma profile across the entire audio signal
        chroma_profile = np.mean(chroma, axis=1)

        # Correlate with major and minor profiles for all 12 keys
        major_correlations = self._correlate_profiles(chroma_profile, self.genre_profile.get_major_profile())
        minor_correlations = self._correlate_profiles(chroma_profile, self.genre_profile.get_minor_profile())

        # Find the key with the highest correlation
        major_key_index = np.argmax(major_correlations)
        minor_key_index = np.argmax(minor_correlations)

        major_key_strength = major_correlations[major_key_index]
        minor_key_strength = minor_correlations[minor_key_index]

        # Define the keys in terms of pitch classes
        keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        # Choose between major and minor based on the highest correlation
        if major_key_strength > minor_key_strength:
            return f"{keys[major_key_index]} major"
        else:
            return f"{keys[minor_key_index]} minor"

    def _correlate_profiles(self, chroma_profile, template_profile):
        """
        Correlates the given chroma profile with the template profile for all 12 key transpositions.

        Args:
            chroma_profile (np.ndarray): The chroma profile of the audio signal.
            template_profile (list): The tonal template profile (either major or minor).

        Returns:
            np.ndarray: An array of correlation values for each key (0-11).
        """
        correlations = []
        for i in range(12):
            rotated_profile = np.roll(template_profile, i)  # Rotate template for all 12 keys
            correlation = np.corrcoef(chroma_profile, rotated_profile)[0, 1]  # Compute Pearson correlation
            correlations.append(correlation)
        return np.array(correlations)