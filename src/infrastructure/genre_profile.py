"""
Module: Genre Profiles
Location: src/infrastructure/genre_profile.py
Defines the base class and genre-specific classes for key-finding profiles.
"""

from abc import ABC, abstractmethod


class GenreProfile(ABC):
    """
    Abstract base class for genre profiles. Subclasses should define major and minor key profiles.
    """

    @abstractmethod
    def __init__(self):
        self.major_profile = []
        self.minor_profile = []

    @abstractmethod
    def get_major_profile(self):
        """
        Returns the major key profile for the genre.
        """

    @abstractmethod
    def get_minor_profile(self):
        """
        Returns the minor key profile for the genre.
        """


class GeneralProfile(GenreProfile):
    """
    General key profile class, default genre profile.
    """

    def __init__(self):
        self.major_profile = [6.0, 2.5, 3.5, 2.5, 4.0, 4.0, 2.5, 5.0, 3.0, 3.5, 2.5, 3.0]
        self.minor_profile = [6.0, 2.5, 3.5, 5.0, 3.0, 3.5, 2.5, 4.8, 4.0, 3.0, 3.5, 3.0]

    def get_major_profile(self):
        return self.major_profile

    def get_minor_profile(self):
        return self.minor_profile


class ClassicalProfile(GenreProfile):
    """
    Classical key profile class.
    """

    def __init__(self):
        self.major_profile = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]
        self.minor_profile = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]

    def get_major_profile(self):
        return self.major_profile

    def get_minor_profile(self):
        return self.minor_profile


class JazzProfile(GenreProfile):
    """
    Jazz key profile class.
    """

    def __init__(self):
        self.major_profile = [5.35, 2.5, 3.3, 3.0, 4.0, 4.5, 2.8, 5.5, 3.5, 4.0, 3.2, 3.5]
        self.minor_profile = [5.2, 3.0, 3.6, 5.0, 3.5, 3.6, 3.0, 5.0, 4.0, 3.8, 3.4, 3.5]

    def get_major_profile(self):
        return self.major_profile

    def get_minor_profile(self):
        return self.minor_profile


class PopProfile(GenreProfile):
    """
    Pop/Rock key profile class.
    """

    def __init__(self):
        self.major_profile = [6.5, 2.5, 3.5, 2.0, 4.5, 4.0, 3.0, 5.0, 3.0, 4.5, 2.0, 2.5]
        self.minor_profile = [6.3, 2.9, 3.7, 5.0, 3.0, 3.5, 2.8, 4.8, 4.2, 2.7, 3.5, 2.8]

    def get_major_profile(self):
        return self.major_profile

    def get_minor_profile(self):
        return self.minor_profile


class BluesProfile(GenreProfile):
    """
    Blues key profile class.
    """

    def __init__(self):
        self.major_profile = [5.8, 2.3, 4.5, 3.2, 4.1, 3.8, 2.6, 4.9, 3.4, 3.7, 2.1, 2.9]
        self.minor_profile = [5.9, 3.1, 3.4, 4.9, 3.7, 3.6, 2.7, 4.2, 4.5, 3.2, 2.7, 3.0]

    def get_major_profile(self):
        return self.major_profile

    def get_minor_profile(self):
        return self.minor_profile


class RockProfile(GenreProfile):
    """
    Rock key profile class.
    """

    def __init__(self):
        self.major_profile = [6.6, 2.6, 3.4, 2.0, 4.3, 4.2, 3.2, 5.1, 3.1, 4.2, 2.3, 2.7]
        self.minor_profile = [6.4, 2.8, 3.9, 5.1, 3.1, 3.2, 2.6, 4.9, 4.3, 2.5, 3.4, 2.6]

    def get_major_profile(self):
        return self.major_profile

    def get_minor_profile(self):
        return self.minor_profile


class MetalProfile(GenreProfile):
    """
    Metal key profile class.
    """

    def __init__(self):
        self.major_profile = [5.9, 2.0, 3.0, 3.8, 4.4, 4.1, 2.9, 5.5, 3.0, 4.0, 3.2, 3.4]
        self.minor_profile = [6.5, 3.2, 3.7, 5.2, 2.9, 3.9, 2.8, 4.8, 4.0, 3.1, 3.6, 2.7]

    def get_major_profile(self):
        return self.major_profile

    def get_minor_profile(self):
        return self.minor_profile


class FlamencoProfile(GenreProfile):
    """
    Flamenco key profile class, using Phrygian scale.
    """

    def __init__(self):
        self.major_profile = [5.2, 2.5, 4.1, 2.7, 3.9, 4.6, 3.1, 5.0, 2.9, 3.8, 2.6, 3.4]
        self.minor_profile = [5.8, 3.0, 3.6, 4.7, 3.1, 3.9, 3.2, 4.9, 3.8, 2.9, 2.7, 3.5]

    def get_major_profile(self):
        return self.major_profile

    def get_minor_profile(self):
        return self.minor_profile