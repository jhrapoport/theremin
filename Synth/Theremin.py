import time
import pyaudio

from . import functions, synth_const


class Theremin:
    def __init__(self, n_notes):
        self.sounds = []
        self.current_note_i = 0
        for i in range(n_notes):
            freq = functions.get_note_freq(i, n_notes)
            note = functions.make_note(freq)
            sound = functions.make_sound(note)
            self.sounds.append(sound)
        self.setup_pyaudio()

    # change the current note playing
    def switch_note(self, note_i):
        self.current_note_i = note_i

    # automatically calls this whenever it needs more sound: returns the current note to be played
    def callback(self, in_data, frame_count, time_info, status):
        data = self.sounds[self.current_note_i]
        return data, pyaudio.paContinue

    # setup all the pyaudio stuff
    def setup_pyaudio(self):
        # start it
        p = pyaudio.PyAudio()
        # open up a stream
        stream = p.open(format=p.get_format_from_width(synth_const.N_BYTES),
                        channels=synth_const.N_CHANNELS, rate=synth_const.FRAME_RATE,
                        output=True, stream_callback=self.callback)
        # and start the stream
        stream.start_stream()

