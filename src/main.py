"""
Main entry point for the music interpreter backend service.
This script sets up the controllers, use cases, and services for the application and processes an audio file.
"""

import os
from src.interface_adapters import AudioUploadController, FeatureExtractionController
from src.use_cases import TranscribeAudioToScore, ExtractMusicalFeatures
from src.infrastructure.librosa_feature_extractor import LibrosaFeatureExtractor
from src.infrastructure.librosa_transcription_service import LibrosaTranscriptionService


def mock_request(file_path):
    """
    Mock request object to simulate a real file upload request.
    Args:
        file_path (str): The path to the audio file to be processed.
    Returns:
        dict: Mocked request object with audio file attributes.
    """
    return {
        'file': {
            'path': file_path,
            'format': 'mp3',
            'duration': 240.0,  # Example duration in seconds
            'sample_rate': 44100  # Standard sample rate for audio files
        }
    }


def get_genre_from_user_input():
    """
    Prompts the user to select a genre and returns the corresponding genre string.

    Returns:
        str: The selected genre ("general", "classical", "jazz", or "pop").
    """
    print("Select the genre for key estimation:")
    print("0: General Profile (default)")
    print("1: Classical")
    print("2: Jazz")
    print("3: Pop")

    try:
        user_input = int(input("Enter the number corresponding to the genre (0-3): "))
    except ValueError:
        print("Invalid input, defaulting to General Profile.")
        return "general"

    if user_input == 1:
        return "classical"
    elif user_input == 2:
        return "jazz"
    elif user_input == 3:
        return "pop"
    else:
        print("Defaulting to General Profile.")
        return "general"


def main():
    """
    Main function to set up the backend services, controllers, and process the sample audio file.
    """
    # Get the genre from user input
    genre = get_genre_from_user_input()

    # Set up the services and use cases using Librosa
    transcription_service = LibrosaTranscriptionService()
    feature_extractor_service = LibrosaFeatureExtractor(genre=genre)

    # Set up use cases
    transcribe_audio_use_case = TranscribeAudioToScore(transcription_service)
    extract_features_use_case = ExtractMusicalFeatures(feature_extractor_service)

    # Set up controllers
    audio_upload_controller = AudioUploadController(transcribe_audio_use_case)
    feature_extraction_controller = FeatureExtractionController(extract_features_use_case)

    # Load the sample audio file
    audio_file_path = '/home/ono/Projects/Audiong/sample_audio/02 - XII. Allegro.flac'

    # Create a mock request object with the audio file details
    request = mock_request(audio_file_path)

    # Process the audio file with the audio upload controller
    print(f"Audio upload and transcription process starts (using Librosa, genre: {genre})...")
    transcription_result = audio_upload_controller.upload_audio(request)
    print(
        f"Transcription Result: MIDI Data (sample): {transcription_result.midi_data[:5]}, Score Data: {transcription_result.score_data[:100]}...")

    # Extract musical features
    print(f"Musical feature extraction starts (using Librosa with K-S algorithm for {genre})...")
    feature_result = feature_extraction_controller.extract_features(request)
    print(
        f"Musical Features - Tempo: {feature_result.tempo}, Key: {feature_result.key}, Pitch: {feature_result.pitch[:10]}, Rhythm: {feature_result.rhythm[:5]}")


if __name__ == "__main__":
    main()