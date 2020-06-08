import threading
import time
import simpleaudio
import const


class Metronome:
    def __init__(self, gui):
        self.gui = gui
        self.tempo = const.DEFAULT_TEMPO
        self.playing_out_loud = False
        self.destructed = False
        self.beat = 0
        t = threading.Thread(target=self.play)
        t.start()

    def change_tempo(self, tempo):
        try:
            self.tempo = float(tempo)
        except ValueError:
            return

    def switch(self):
        if self.playing_out_loud:
            self.off()
            return False
        else:
            self.on()
            return True

    def on(self):
        self.playing_out_loud = True

    def off(self):
        self.playing_out_loud = False
        self.beat = 0

    def play(self):
        while not self.destructed:
            self.gui.beat()
            if self.playing_out_loud:
                if self.beat != 3:  # click
                    simpleaudio.WaveObject.from_wave_file("metsound1.wav").play()
                else:               # clack
                    simpleaudio.WaveObject.from_wave_file("metsound2.wav").play()
                self.beat = (self.beat + 1) % 4
            time.sleep(60/self.tempo)

    def destruct(self):
        self.destructed = True

