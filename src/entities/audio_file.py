"""
Module: Audio File Entity
Location: entities/audio_file.py
Defines the core entity for handling uploaded audio files in the music interpreter service.
"""


class AudioFile:
    """
    Represents an uploaded audio file.

    Attributes:
        file_path (str): Path to the uploaded audio file on the system or cloud storage.
        format (str): Audio file format, such as 'wav', 'mp3', etc.
        duration (float): The duration of the audio file in seconds.
        sample_rate (int): The sample rate of the audio file in Hertz.
    """

    def __init__(self, file_path: str, format: str, duration: float, sample_rate: int):
        self.file_path = file_path
        self.format = format
        self.duration = duration
        self.sample_rate = sample_rate