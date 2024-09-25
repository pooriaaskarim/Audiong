"""
Module: Transcription Result Entity
Location: entities/transcription_result.py
Defines the entity for holding the result of an audio transcription, including MIDI and MusicXML data.
"""


class TranscriptionResult:
    """
    Represents the result of transcribing audio into music notation.

    Attributes:
        midi_data (bytes): The byte representation of the transcribed MIDI file.
        score_data (str): The MusicXML representation of the music score.
    """

    def __init__(self, midi_data: bytes, score_data: str):
        self.midi_data = midi_data
        self.score_data = score_data