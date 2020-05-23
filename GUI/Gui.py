import tkinter as tk
from . import gui_const
from Synth import Theremin


class Gui:
    def __init__(self):
        self.note_playing = None
        self.theremin = Theremin.Theremin(gui_const.WINDOW_LENGTH)
        self.window = tk.Tk()
        self.config()
        self.run()

    def run(self):
        self.window.mainloop()

    def on_motion(self, event):
        self.theremin.switch_note(event.x)

    def config(self):
        self.window.bind("<Motion>", self.on_motion)
        self.window.geometry(gui_const.WINDOW_DIMENSIONS)
        self.window.resizable(0, 0)
