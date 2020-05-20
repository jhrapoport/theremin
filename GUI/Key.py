import tkinter as tk
from GUI import gui_const


class Key:
    def __init__(self, window, piano, key_number):
        self.piano = piano
        self.button = tk.Button(window, height=gui_const.KEY_HEIGHT,
                                width=gui_const.KEY_WIDTH, bg="white")
        self.key_number = key_number
        self.button.grid(column=key_number, row=gui_const.ROW)
        self.button.bind('<ButtonPress>', lambda event: self.pushed())
        self.button.bind('<ButtonRelease>', lambda event: self.released())

    def pushed(self):
        self.piano.start_sound(self.key_number)

    def released(self):
        self.piano.end_sound(self.key_number)

