"""
Entities module for the music interpreter service.
Contains the core domain models.
"""

from .audio_file import AudioFile
from .music_score import MusicScore
from .musical_feature import MusicalFeature
from .transcription_result import TranscriptionResult

__all__ = ['AudioFile', 'MusicScore', 'MusicalFeature', 'TranscriptionResult']