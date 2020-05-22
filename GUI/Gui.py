import tkinter as tk
from . import gui_const
from Synth import Theremin


class Gui:
    def __init__(self):
        self.note_playing = None
        self.theremin = Theremin.Theremin()
        self.window = tk.Tk()
        self.config()
        self.run()

    def run(self):
        self.window.mainloop()

    def on_motion(self, event):
        if self.note_playing:
            if abs(self.note_playing - event.x) < 10:
                return
            self.theremin.end_sound(self.note_playing, gui_const.WINDOW_LENGTH)
        self.theremin.start_sound(event.x, gui_const.WINDOW_LENGTH)
        self.note_playing = event.x

    def config(self):
        self.window.bind("<Motion>", self.on_motion)
        self.window.geometry(gui_const.WINDOW_DIMENSIONS)
