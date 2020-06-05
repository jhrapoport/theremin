import tkinter as tk
from PIL import ImageTk, Image
import gui_const
import Theremin


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
        self.theremin.switch_sound(490 - abs(490 - event.x), gui_const.WINDOW_HEIGHT - event.y - 1)

    def on_close(self):
        self.theremin.destruct()
        self.window.destroy()

    def config(self):
        self.window.configure(cursor="hand1 black")
        self.window.bind("<Motion>", self.on_motion)
        self.window.geometry(gui_const.WINDOW_DIMENSIONS)
        self.window.resizable(0, 0)
        self.window.title("Theremin")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        theremin_img = ImageTk.PhotoImage(Image.open("theremin.png"))
        label = tk.Label(self.window, image=theremin_img)
        label.image = theremin_img
        label.place(x=0, y=30)

