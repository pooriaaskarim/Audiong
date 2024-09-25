"""
Module: Musical Feature Entity
Location: entities/musical_feature.py
Defines the entity for holding extracted musical features such as tempo, key, pitch, and rhythm.
"""

class MusicalFeature:
    """
    Represents musical features extracted from an audio file.

    Attributes:
        tempo (float): The tempo of the music in BPM (beats per minute).
        key (str): The musical key (e.g., "C major").
        pitch (list): List of pitch values detected in the audio.
        rhythm (list): List of rhythmic patterns in the audio.
    """

    def __init__(self, tempo: float, key: str, pitch: list, rhythm: list):
        self.tempo = tempo
        self.key = key
        self.pitch = pitch
        self.rhythm = rhythm