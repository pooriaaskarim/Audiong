import sounddevice as sd
import numpy as np
import librosa
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
from matplotlib.widgets import Button, TextBox

class RealTimeTranscriber:
    def __init__(self, sample_rate=44100, buffer_size=2048, pitch_sensitivity=0.1):
        self.sample_rate = sample_rate
        self.buffer_size = buffer_size
        self.buffer = deque(maxlen=int(sample_rate / buffer_size))
        self.pitch_sensitivity = pitch_sensitivity

        # Set up the figure for real-time plotting
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.25)
        self.ax.set_facecolor('#001f3f')  # Dark blue background
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Frequency (Hz)")
        self.ax.set_xlim(0, 10)  # Time axis (10 seconds window)
        self.ax.set_ylim(20, 4200)  # Frequency range for musical notes (A0 ~ 27.5 Hz to C8 ~ 4186 Hz)

        self.notes_data = {}  # Dictionary to track active notes

        # Create buttons and text box
        self.restart_button_ax = plt.axes([0.7, 0.02, 0.1, 0.075])
        self.restart_button = Button(self.restart_button_ax, 'Restart')
        self.restart_button.on_clicked(self.restart_transcription)

        self.duration_box_ax = plt.axes([0.4, 0.02, 0.1, 0.075])
        self.duration_box = TextBox(self.duration_box_ax, 'Duration (s)', initial='10')

        # Store the animation reference and current duration
        self.anim = None
        self.duration = 10

    def audio_callback(self, indata, frames, time, status):
        audio_chunk = indata[:, 0]
        self.buffer.append(audio_chunk)

    def pitch_to_frequency(self, pitch):
        if pitch > 0:
            return librosa.midi_to_hz(pitch)
        return None

    def detect_pitch(self, audio_chunk):
        pitches, magnitudes = librosa.piptrack(y=audio_chunk, sr=self.sample_rate)

        pitch_idx = magnitudes.argmax(axis=0)
        pitch_values = pitches[pitch_idx, np.arange(pitches.shape[1])]
        magnitudes_values = magnitudes[pitch_idx, np.arange(magnitudes.shape[1])]

        non_zero_indices = pitch_values > 0
        if np.any(non_zero_indices):
            pitch = pitch_values[non_zero_indices].max()  # Highest pitch detected
            intensity = magnitudes_values[non_zero_indices].max()  # Corresponding intensity

            if 21 <= pitch <= 108:
                return pitch, intensity
        return None, None

    def update_active_notes(self, current_time, frequency, intensity):
        if frequency in self.notes_data:
            self.notes_data[frequency]['end_time'] = current_time
            self.notes_data[frequency]['intensity'] = intensity
        else:
            self.notes_data[frequency] = {
                'start_time': current_time,
                'end_time': current_time,
                'intensity': intensity
            }

    def remove_inactive_notes(self, current_time):
        to_remove = [frequency for frequency, note_data in self.notes_data.items()
                     if current_time - note_data['end_time'] > self.pitch_sensitivity]
        for frequency in to_remove:
            del self.notes_data[frequency]

    def restart_transcription(self, event):
        self.notes_data.clear()

        try:
            self.duration = int(self.duration_box.text)
        except ValueError:
            self.duration = 10  # Default to 10 seconds if invalid input

        self.ax.clear()
        self.ax.set_xlim(0, self.duration)
        self.ax.set_ylim(20, 4200)
        self.ax.set_facecolor('#001f3f')  # Dark blue background

        if self.anim:
            self.anim.event_source.stop()
        self.start_transcription(self.duration)

    def start_transcription(self, duration=10):
        with sd.InputStream(callback=self.audio_callback, channels=1, samplerate=self.sample_rate, blocksize=self.buffer_size):
            print("Starting real-time transcription... Press Ctrl+C to stop.")
            plt.ion()

            self.animate_plot(duration)

    def animate_plot(self, duration):
        def update(frame):
            current_time = frame / 10.0

            if len(self.buffer) > 0:
                audio_chunk = np.concatenate(list(self.buffer))
                pitch, intensity = self.detect_pitch(audio_chunk)

                if pitch:
                    frequency = self.pitch_to_frequency(pitch)
                    if frequency:
                        self.update_active_notes(current_time, frequency, intensity)
                        note_name = librosa.hz_to_note(frequency)

                        # Debug info: print details for each detected note
                        print(f"Time: {current_time:.2f}s, Note: {note_name}, Frequency: {frequency:.2f}Hz, "
                              f"Intensity: {intensity:.2f}")
                else:
                    # Debug when no pitch detected
                    print(f"Time: {current_time:.2f}s, No pitch detected.")

                self.remove_inactive_notes(current_time)

                self.ax.clear()
                self.ax.set_facecolor('#001f3f')

                time_window = max(0.1, current_time - duration)
                self.ax.set_xlim(time_window, current_time)
                self.ax.set_ylim(20, 4200)

                for frequency, note_data in self.notes_data.items():
                    start_time = note_data['start_time']
                    end_time = note_data['end_time']
                    intensity = note_data['intensity']

                    opacity = intensity / max(intensity, 1.0)
                    line_width = 5

                    self.ax.hlines(frequency, start_time, end_time, color='white', linewidth=line_width, alpha=opacity)
                    note_name = librosa.hz_to_note(frequency)
                    self.ax.text(start_time, frequency, note_name, fontsize=12, color='#001f3f',
                                 verticalalignment='center', horizontalalignment='left')

                self.ax.set_xlabel("Time (s)")
                self.ax.set_ylabel("Frequency (Hz)")
                plt.pause(0.01)

            return self.ax

        self.anim = FuncAnimation(self.fig, update, frames=np.linspace(0, duration, int(duration * 10)), repeat=False)
        plt.show(block=True)

# Example usage:
transcriber = RealTimeTranscriber()
transcriber.start_transcription(10)