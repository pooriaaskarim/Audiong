"""
Main entry point for the music interpreter backend service.
This script sets up the controllers, use cases, and services for the application and processes an audio file.
"""

from src.interface_adapters import AudioUploadController, FeatureExtractionController
from src.use_cases import TranscribeAudioToScore, ExtractMusicalFeatures
from src.infrastructure import LibrosaTranscriptionService, LibrosaFeatureExtractor

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

def main():
    """
    Main function to set up the backend services, controllers, and process the sample audio file.
    """
    # Set up the services and use cases
    transcription_service = LibrosaTranscriptionService()
    feature_extractor_service = LibrosaFeatureExtractor()

    # Set up use cases
    transcribe_audio_use_case = TranscribeAudioToScore(transcription_service)
    extract_features_use_case = ExtractMusicalFeatures(feature_extractor_service)

    # Set up controllers
    audio_upload_controller = AudioUploadController(transcribe_audio_use_case)
    feature_extraction_controller = FeatureExtractionController(extract_features_use_case)

    # Load the sample audio file
    # audio_file_path = '/home/ono/Projects/Audiong/sample_audio/Disturbed-in-the-Wind.mp3'
    audio_file_path = '/home/ono/Projects/Audiong/sample_audio/Grieg_Cello_Sonata_in_A_minor_M_Maisky,_M_Argerich_1st_Movement.mp3'
    # audio_file_path = '/home/ono/Projects/Audiong/sample_audio/Knife Edge.mp3'
    # audio_file_path = '/home/ono/Projects/Audiong/sample_audio/Thom_Yorke_Ft_Flea_Daily_Battle.mp3'

    # Create a mock request object with the audio file details
    request = mock_request(audio_file_path)

    # Process the audio file with the audio upload controller
    print("Audio upload and transcription process starts...")
    transcription_result = audio_upload_controller.upload_audio(request)
    print(f"Transcription Result: MIDI Data (sample): {transcription_result.midi_data[:5]}, Score Data: {transcription_result.score_data[:100]}...")

    # Extract musical features
    print("Musical feature extraction starts...")
    feature_result = feature_extraction_controller.extract_features(request)
    print(f"Musical Features - Tempo: {feature_result.tempo}, Key: {feature_result.key}, Pitch: {feature_result.pitch[:10]}, Rhythm: {feature_result.rhythm[:5]}")

if __name__ == "__main__":
    main()