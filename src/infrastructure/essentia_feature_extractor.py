# """
# Module: Essentia Feature Extractor
# Location: src/infrastructure/essentia_feature_extractor.py
# Implements the extraction of musical features using the Essentia library.
# """
#
# import essentia.standard as es
# from src.entities.audio_file import AudioFile
#
# class EssentiaFeatureExtractor:
#     """
#     Implements the extraction of musical features (tempo, key, pitch, rhythm) from audio files using Essentia.
#
#     Methods:
#         extract: Extracts musical features from the given audio file.
#     """
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
#         # Estimate key
#         key_extractor = es.KeyExtractor()
#         key, scale, strength = key_extractor(audio)
#
#         # Extract pitch using PitchYin algorithm
#         pitch_extractor = es.PitchYin()
#         pitch_values = []
#         for frame in es.FrameGenerator(audio, frameSize=2048, hopSize=1024, startFromZero=True):
#             pitch, confidence = pitch_extractor(frame)
#             if confidence > 0.9:  # Confidence threshold to filter noise
#                 pitch_values.append(pitch)
#
#         # Rhythm (time of beats)
#         rhythm = beats
#
#         return {
#             "tempo": bpm,
#             "key": f"{key} {scale}",
#             "pitch": pitch_values[:10],  # Return first 10 pitch values for simplicity
#             "rhythm": rhythm.tolist()    # Convert numpy array to list
#         }