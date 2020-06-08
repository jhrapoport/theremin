import threading
import time
import simpleaudio
import const


class Metronome:
    def __init__(self):
        self.tempo = const.DEFAULT_TEMPO
        self.playing = False
        self.beat = 0

    def change_tempo(self, tempo):
        try:
            self.tempo = float(tempo)
        except ValueError:
            return

    def switch(self):
        if self.playing:
            self.off()
            return False
        else:
            self.on()
            return True

    def on(self):
        self.playing = True
        t = threading.Thread(target=self.play)
        t.start()

    def off(self):
        self.playing = False
        self.beat = 0

    def play(self):
        while self.playing:
            if self.beat != 3:
                simpleaudio.WaveObject.from_wave_file("metsound1.wav").play()
            else:
                simpleaudio.WaveObject.from_wave_file("metsound2.wav").play()
            self.beat = (self.beat + 1) % 4
            time.sleep(60/self.tempo)

