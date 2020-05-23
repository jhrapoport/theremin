import time
import pyaudio

from . import functions, synth_const


class Theremin:
    def __init__(self, n_tones, n_volumes):
        self.sounds = []
        self.current_tone_i = 0
        self.current_volume_i = 0
        # make all the musical tones
        for i in range(n_tones):
            freq = functions.get_tone_freq(i, n_tones)
            tone = functions.make_tone(freq)
            self.sounds.append([])
            # make all the volume options for the current tone
            for j in range(n_volumes):
                # make that current sound
                sound = functions.make_sound(tone, j, n_volumes)
                # add it to the 2D array of sounds
                self.sounds[-1].append(sound)
        self.setup_pyaudio()

    # change the current tone playing
    def switch_sound(self, tone_i, volume_i):
        self.current_tone_i = tone_i
        self.current_volume_i = volume_i

    # automatically calls this whenever it needs more sound: returns the current tone to be played
    def callback(self, in_data, frame_count, time_info, status):
        print("(", end = "")
        print(self.current_tone_i, end = "/")
        print(len(self.sounds), end = ", ")
        print(self.current_volume_i, end = "/")
        print(len(self.sounds[0]), end = ")")
        print()
        data = self.sounds[self.current_tone_i][self.current_volume_i]
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

