import simpleaudio

from . import functions, synth_const


class Theremin:
    def __init__(self):
        self.play = True
        self.record = False
        self.sounds = []
        self.players = []

        for i in range(synth_const.N_TONES):
            freq = functions.get_pixels_freq(i)
            note = functions.make_note(freq)
            sound = functions.make_sound(note)
            self.sounds.append(sound)
            self.players.append(None)

    def start_sound(self, note_pixel, max_pixel):
        note_i = int(synth_const.N_TONES*note_pixel/max_pixel)
        if self.play:
            self.start_playing(note_i)
        if self.record:
            self.start_recording(note_i)

    def end_sound(self, note_pixel, max_pixel):
        note_i = int(synth_const.N_TONES*note_pixel/max_pixel)
        if self.play:
            self.stop_playing(note_i)
        if self.record:
            self.stop_recording(note_i)

    def start_playing(self, note_i):
        sound = self.sounds[note_i]
        self.players[note_i] = simpleaudio.play_buffer(sound, 1, 2, synth_const.FRAME_RATE)

    def stop_playing(self, note_i):
        self.players[note_i].stop()
        self.players[note_i] = None

    def start_recording(self, note_i):
        pass

    def stop_recording(self, note_i):
        pass
