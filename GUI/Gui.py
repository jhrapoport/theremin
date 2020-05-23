import tkinter as tk
from . import gui_const
from Synth import Theremin


class Gui:
    def __init__(self):
        self.note_playing = None
        self.theremin = Theremin.Theremin(gui_const.WINDOW_LENGTH, gui_const.WINDOW_HEIGHT)
        self.window = tk.Tk()
        self.config()
        self.run()

    def run(self):
        self.window.mainloop()

    def on_motion(self, event):
        self.theremin.switch_sound(event.x, gui_const.WINDOW_HEIGHT - event.y - 1)

    def config(self):
        self.window.bind("<Motion>", self.on_motion)
        self.window.geometry(gui_const.WINDOW_DIMENSIONS)
        self.window.resizable(0, 0)
