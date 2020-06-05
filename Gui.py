import tkinter as tk
import const
import Theremin


class Gui:
    def __init__(self):
        self.note_playing = None
        self.theremin = Theremin.Theremin(const.CANVAS_LENGTH / 2, const.CANVAS_HEIGHT)
        self.window = tk.Tk()
        self.config()
        self.run()

    def run(self):
        self.window.mainloop()

    def on_motion(self, event):
        distance = abs(const.CANVAS_LENGTH / 2 - event.x)
        height = const.CANVAS_HEIGHT - event.y - 1
        self.theremin.switch_sound(distance, height)

    def on_close(self):
        self.theremin.destruct()
        self.window.destroy()

    def config(self):
        self.window.configure(background=const.BG_COLOR)
        self.window.title("Theremin")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        canvas = tk.Canvas(self.window, width=const.CANVAS_LENGTH, height=const.CANVAS_HEIGHT,
                           background=const.CANVAS_COLOR)
        canvas.grid(column=0, row=0)
        canvas.configure(cursor="hand1 black")
        canvas.bind("<Motion>", self.on_motion)

