import time
import threading
import numpy
import sounddevice


class Theremin:
    def __init__(self):
        self.sin_start = 0
        self.sin_up = True
        self.amp = 0
        self.freq = 0
        self.samplerate = sounddevice.query_devices(None, 'output')['default_samplerate']
        self.playing = True
        self.start_sound()

    # change the current sound playing
    def switch_sound(self, freq, amp):
        self.freq = freq
        self.amp = amp

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

    # get the number of frames we need to skip ahead to make this sin wave start where last left off
    def get_sin_offset(self, frames):
        test_t = (numpy.arange(frames)) / self.samplerate
        test_t = test_t.reshape(-1, 1)
        test_t = self.amp * numpy.sin(2 * numpy.pi * self.freq * test_t)
        # try to find a good match
        for i in range(frames - 1):
            # if the sine wave was on an upswing, check for that case
            if self.sin_up:
                if test_t[i] <= self.sin_start <= test_t[i + 1]:
                    return i
            # if the sine wave was on a downswing, check for that case
            else:
                if test_t[i] >= self.sin_start >= test_t[i + 1]:
                    return i

        # if no good match found, then find a mediocre matchc
        closest_i = -1
        closest_difference = 99999
        for i in range(frames - 1):
            difference = abs(test_t[i] - self.sin_start)
            if difference < closest_difference:
                closest_i = i
        return closest_i

    def callback(self, outdata, frames, time, status):
        sin_offset = self.get_sin_offset(frames)
        t = (sin_offset + numpy.arange(frames)) / self.samplerate
        t = t.reshape(-1, 1)
        outdata[:] = self.amp * numpy.sin(2 * numpy.pi * self.freq * t)
        # get the last insantaneous sine value so next wave can match up with it
        self.sin_start = float(outdata[-1])
        # check whether that wave was going up or down
        self.sin_up = float(outdata[-1]) > float(outdata[-2])

    def pause(self):
        self.switch_sound(0, 0)

    def destruct(self):
        self.playing = False
