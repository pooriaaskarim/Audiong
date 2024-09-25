"""
Module: Transcribe Audio to Score Use Case
Location: use_cases/transcribe_audio_to_score.py
Defines the use case for transcribing audio into a musical score.
"""

from src.entities.transcription_result import TranscriptionResult
from src.entities.audio_file import AudioFile


class TranscribeAudioToScore:
    """
    Use case for transcribing an audio file into a musical score.

    Attributes:
        transcription_service: A service that handles the transcription process (audio to score).
    """

    def __init__(self, transcription_service):
        self.transcription_service = transcription_service

    def execute(self, audio_file: AudioFile) -> TranscriptionResult:
        """
        Executes the transcription of the given audio file.

        Args:
            audio_file (AudioFile): The audio file to be transcribed.

        Returns:
            TranscriptionResult: The result containing MIDI data and MusicXML score data.
        """
        midi_data, score_data = self.transcription_service.transcribe(audio_file)
        return TranscriptionResult(midi_data, score_data)