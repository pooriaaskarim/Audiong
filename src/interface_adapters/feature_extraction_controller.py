"""
Module: Feature Extraction Controller
Location: interface_adapters/feature_extraction_controller.py
Handles the request for extracting musical features from an audio file and invoking the relevant use case.
"""

from src.entities.audio_file import AudioFile
from src.use_cases.extract_musical_features import ExtractMusicalFeatures


class FeatureExtractionController:
    """
    Controller to handle requests for extracting musical features from audio files.

    Attributes:
        extract_musical_features_use_case (ExtractMusicalFeatures): The use case for extracting musical features.
    """

    def __init__(self, extract_musical_features_use_case: ExtractMusicalFeatures):
        self.extract_musical_features_use_case = extract_musical_features_use_case

    def extract_features(self, request):
        """
        Handles the request to extract musical features from an uploaded audio file.

        Args:
            request: The incoming request object that contains the audio file.

        Returns:
            MusicalFeature: The extracted musical features.
        """
        audio_file = AudioFile(
            file_path=request['file']['path'],
            format=request['file']['format'],
            duration=request['file']['duration'],
            sample_rate=request['file']['sample_rate']
        )
        features = self.extract_musical_features_use_case.execute(audio_file)
        return features