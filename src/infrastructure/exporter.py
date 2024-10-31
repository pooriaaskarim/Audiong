"""
Module: Music Exporter
Location: src/infrastructure/exporter.py
Exports extracted musical features to MIDI and MusicXML formats.
"""

from music21 import stream, note, meter, key as m21key
import mido

class MusicExporter:
    """
    A class to export musical features (pitch, rhythm) to MIDI and MusicXML formats.
    """

    @staticmethod
    def export_to_midi(pitches, rhythm, output_path):
        """
        Export the extracted features to a MIDI file.
        
        Args:
            pitches (np.ndarray): Pitch values (Hz) to export.
            rhythm (list): Rhythm values (timings) to export.
            output_path (str): Path to save the MIDI file.
        """
        midi_file = mido.MidiFile()
        track = mido.MidiTrack()
        midi_file.tracks.append(track)

        for i in range(len(pitches)):
            midi_note = int(librosa.hz_to_midi(pitches[i]))
            duration = int(rhythm[i] * 480)  # Convert rhythm to MIDI ticks
            track.append(mido.Message('note_on', note=midi_note, velocity=64, time=0))
            track.append(mido.Message('note_off', note=midi_note, velocity=64, time=duration))

        midi_file.save(output_path)
        print(f"MIDI file saved to {output_path}")

    @staticmethod
    def export_to_musicxml(pitches, rhythm, key_str, voice_type, output_dir="exports"):
        """
        Export the extracted features to a MusicXML file for a single voice.

        Args:
            pitches (np.ndarray): Pitch values (Hz) to export.
            rhythm (list): Rhythm values (timings) to export.
            key_str (str): Musical key signature (e.g., "C major").
            voice_type (str): The type of voice (vocals, drums, bass, etc.).
            output_dir (str): Directory to save the MusicXML file.
        """
        score = stream.Score()
        score.append(meter.TimeSignature('4/4'))

        k = m21key.Key(key_str.split()[0], key_str.split()[1])
        score.append(k)

        for i in range(len(pitches)):
            if rhythm[i] < 0.03125:
                continue
            n = note.Note()
            n.pitch.frequency = pitches[i]
            n.quarterLength = max(rhythm[i], 0.03125)
            score.append(n)

        output_path = f"{output_dir}/{voice_type}.xml"
        score.write('musicxml', fp=output_path)
        print(f"MusicXML file saved to {output_path}")