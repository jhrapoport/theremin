import tkinter as tk
from . import Key, gui_const
from Synth import Piano


class Gui:
    def __init__(self):
        self.piano = Piano.Piano()
        self.window = tk.Tk()
        self.add_components()
        self.run()

    def run(self):
        self.window.mainloop()

    def add_components(self):
        for i in range(gui_const.N_KEYS):
            Key.Key(self.window, self.piano, i)
