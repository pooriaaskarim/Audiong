"""
Module: Extract Musical Features Use Case
Location: use_cases/extract_musical_features.py
Defines the use case for extracting musical features from an audio file.
"""
from src.entities.audio_file import AudioFile
from src.entities.musical_feature import MusicalFeature


class ExtractMusicalFeatures:
    """
    Use case for extracting musical features such as tempo, key, pitch, and rhythm
     from an audio file.

    Attributes:
        feature_extractor: A service responsible for extracting musical
         features from the audio file.
    """

    def __init__(self, feature_extractor):
        self.feature_extractor = feature_extractor

    def execute(self, audio_file: AudioFile) -> MusicalFeature:
        """
        Executes the extraction of musical features from the audio file.

        Args:
            audio_file (AudioFile): The audio file to extract features from.

        Returns:
            MusicalFeature: An object containing the extracted musical features.
        """
        features = self.feature_extractor.extract(audio_file)
        return MusicalFeature(
            tempo=features["tempo"],
            key=features["key"],
            pitch=features["pitch"],
            rhythm=features["rhythm"]
        )