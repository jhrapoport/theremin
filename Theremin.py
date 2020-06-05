import time
import threading

import numpy
import sounddevice

import synth_const


class Theremin:
    def __init__(self, max_freq_i, max_amp_i):
        self.amp = 0
        self.freq = 0
        self.max_freq_i = max_freq_i
        self.max_amp_i = max_amp_i
        self.samplerate = sounddevice.query_devices(None, 'output')['default_samplerate']
        self.playing = True
        self.start_sound()

    # change the current sound playing
    def switch_sound(self, freq_i, amp_i):
        self.amp = synth_const.MAX_AMP * amp_i / self.max_amp_i
        self.freq = synth_const.MIN_FREQ + \
                    (synth_const.MAX_FREQ - synth_const.MIN_FREQ) * freq_i / self.max_freq_i

    # make the sound start playing
    def start_sound(self):
        # make a thread for this so the gui and the sound can run concurrently
        t = threading.Thread(target=self.make_sound_thread)
        t.start()

    def make_sound_thread(self):
        with sounddevice.OutputStream(device=sounddevice.default.device, channels=1, callback=self.callback,
                                      samplerate=self.samplerate):
            # check once per second whether to stop playing
            while self.playing:
                time.sleep(1)

    def callback(self, outdata, frames, time, status):
        t = numpy.arange(frames) / self.samplerate
        t = t.reshape(-1, 1)
        outdata[:] = self.amp * numpy.sin(2 * numpy.pi * self.freq * t)

    def destruct(self):
        self.playing = False