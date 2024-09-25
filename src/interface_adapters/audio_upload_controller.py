"""
Module: Audio Upload Controller
Location: interface_adapters/audio_upload_controller.py
Handles the HTTP request for uploading an audio file and invoking the transcription use case.
"""
from src.entities.audio_file import AudioFile
from src.use_cases.transcribe_audio_to_score import TranscribeAudioToScore


class AudioUploadController:
    """
    Controller to handle audio file uploads and trigger the transcription use case.

    Attributes:
        transcribe_audio_to_score_use_case (TranscribeAudioToScore): The use case for audio transcription.
    """

    def __init__(self, transcribe_audio_to_score_use_case: TranscribeAudioToScore):
        self.transcribe_audio_to_score_use_case = transcribe_audio_to_score_use_case

    def upload_audio(self, request):
        """
        Handles the audio upload request, converts it to an AudioFile entity, and invokes the transcription use case.

        Args:
            request: The incoming request object that contains the audio file.

        Returns:
            TranscriptionResult: The result of the audio transcription process.
        """
        audio_file = AudioFile(
            file_path=request['file']['path'],
            format=request['file']['format'],
            duration=request['file']['duration'],
            sample_rate=request['file']['sample_rate']
        )
        result = self.transcribe_audio_to_score_use_case.execute(audio_file)
        return result