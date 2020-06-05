import tkinter as tk
import gui_const
import Theremin


class Gui:
    def __init__(self):
        self.note_playing = None
        self.theremin = Theremin.Theremin(gui_const.CANVAS_LENGTH/2, gui_const.CANVAS_HEIGHT)
        self.window = tk.Tk()
        self.config()
        self.run()

    def run(self):
        self.window.mainloop()

    def on_motion(self, event):
        distance = abs(gui_const.CANVAS_LENGTH/2 - event.x)
        height = gui_const.CANVAS_HEIGHT - event.y - 1
        self.theremin.switch_sound(distance, height)

    def on_close(self):
        self.theremin.destruct()
        self.window.destroy()

    def config(self):
        self.window.configure(background=gui_const.BG_COLOR)
        self.window.title("Theremin")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        canvas = tk.Canvas(self.window, width=gui_const.CANVAS_LENGTH, height=gui_const.CANVAS_HEIGHT,
                           background=gui_const.CANVAS_COLOR)
        canvas.grid(column=0, row=0)
        canvas.configure(cursor="hand1 black")
        canvas.bind("<Motion>", self.on_motion)

