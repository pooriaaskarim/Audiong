# """
# Module: Essentia Feature Extractor with K-S Algorithm
# Location: src/infrastructure/essentia_feature_extractor.py
# Implements the extraction of musical features using the Essentia library,
# with key estimation handled by the Krumhansl-Schmuckler algorithm.
# """
#
# import essentia.standard as es
# from src.infrastructure.ks_key_finder import KrumhanslSchmucklerKeyFinder
# from entities.audio_file import AudioFile
#
# class EssentiaFeatureExtractor:
#     """
#     Implements the extraction of musical features (tempo, key, pitch, rhythm) from audio files using Essentia,
#     and uses the Krumhansl-Schmuckler algorithm for key estimation.
#
#     Methods:
#         extract: Extracts musical features from the given audio file.
#     """
#
#     def __init__(self):
#         self.ks_key_finder = KrumhanslSchmucklerKeyFinder()
#
#     def extract(self, audio_file: AudioFile):
#         """
#         Extracts musical features such as tempo, key, pitch, and rhythm from the audio file.
#
#         Args:
#             audio_file (AudioFile): The audio file to extract features from.
#
#         Returns:
#             dict: A dictionary containing tempo, key, pitch, and rhythm data.
#         """
#         # Load the audio file using Essentia
#         loader = es.MonoLoader(filename=audio_file.file_path, sampleRate=audio_file.sample_rate)
#         audio = loader()
#
#         # Extract tempo
#         rhythm_extractor = es.RhythmExtractor2013()
#         bpm, beats, _, _, _ = rhythm_extractor(audio)
#
#         # Use K-S algorithm to estimate key
#         key = self.ks_key_finder.estimate_key(audio_file.file_path, audio_file.sample_rate)
#
#         # Extract pitch using PitchYin algorithm
#         pitch_extractor = es.PitchYin()
#         pitch_values = []
#         for frame in es.FrameGenerator(audio, frameSize=2048, hopSize=1024, startFromZero=True):
#             pitch, confidence = pitch_extractor(frame)
#             if confidence > 0.9:
#                 pitch_values.append(pitch)
#
#         # Rhythm (time of beats)
#         rhythm = beats
#
#         return {
#             "tempo": bpm,
#             "key": key,
#             "pitch": pitch_values[:10],  # Return first 10 pitch values for simplicity
#             "rhythm": rhythm.tolist()    # Convert numpy array to list
#         }