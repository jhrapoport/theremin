import simpleaudio

from . import note_maker, freq_calc, synth_const, sound_maker


class Piano:
    def __init__(self):
        self.play_live = True
        self.record = False
        self.sounds = []
        self.players = []

        for i in range(synth_const.N_KEYS):
            freq = freq_calc.get_freq(synth_const.FIRST_KEY, i)
            note = note_maker.make_note(freq)
            sound = sound_maker.make_sound(note)
            self.sounds.append(sound)
            self.players.append(None)

    def start_sound(self, key_i):
        if self.play_live:
            self.start_playing(key_i)
        if self.record:
            self.start_recording(key_i)

    def end_sound(self, key_i):
        if self.play_live:
            self.stop_playing(key_i)
        if self.record:
            self.stop_recording(key_i)

    def start_playing(self, key_i):
        sound = self.sounds[key_i]
        self.players[key_i] = simpleaudio.play_buffer(sound, 1, 2, synth_const.FRAME_RATE)

    def stop_playing(self, key_i):
        self.players[key_i].stop()
        self.players[key_i] = None

    def start_recording(self, key_i):
        pass

    def stop_recording(self, key_i):
        pass
