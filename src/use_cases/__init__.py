"""
Use Cases module for the music interpreter service.
Contains the application-specific business logic.
"""

from .transcribe_audio_to_score import TranscribeAudioToScore
from .extract_musical_features import ExtractMusicalFeatures

__all__ = ['TranscribeAudioToScore', 'ExtractMusicalFeatures']