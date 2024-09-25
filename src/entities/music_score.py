"""
Module: Music Score Entity
Location: entities/music_score.py
Defines the entity that stores the result of music transcription as a score.
"""


class MusicScore:
    """
    Represents a musical score generated from an audio file.

    Attributes:
        title (str): The title of the music piece.
        composer (str): Composer of the piece (optional).
        notes (list): A list of musical notes in the score.
    """

    def __init__(self, title: str, composer: str = None):
        self.title = title
        self.composer = composer
        self.notes = []

    def add_notes(self, notes: list):
        """
        Adds notes to the musical score.
        
        Args:
            notes (list): List of musical notes.
        """
        self.notes.extend(notes)