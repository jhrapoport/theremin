import threading
import time
import const


class Metronome:
    def __init__(self):
        self.tempo = const.DEFAULT_TEMPO
        self.playing = False
        self.temp = 0

    def change_tempo(self, tempo):
        self.tempo = tempo

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

    def play(self):
        while self.playing:
            print(self.temp)
            self.temp += 1
            time.sleep(60/self.tempo)




