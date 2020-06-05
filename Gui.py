import tkinter as tk
import tkinter.font as font
import const
import Theremin


class Gui:
    def __init__(self):
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
        self.config_window()
        self.add_canvas()
        self.add_widgets()

    def config_window(self):
        self.window.configure(background=const.BG_COLOR)
        self.window.title("Theremin")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def add_canvas(self):
        canvas = tk.Canvas(self.window, width=const.CANVAS_LENGTH, height=const.CANVAS_HEIGHT,
                           background=const.CANVAS_COLOR)
        canvas.grid(column=0, row=0, columnspan=5, rowspan=5)
        canvas.configure(cursor="hand1 black")
        canvas.bind("<Motion>", self.on_motion)

    def add_widgets(self):
        volume_slider = tk.Scale(self.window, command=lambda x: self.change_volume(x))
        volume_slider.config(background="darkgray", from_=0.0, to=1.0, resolution=0.01, length=64)
        volume_slider.config(label="Volume", orient=tk.HORIZONTAL, showvalue=0, sliderlength=15)
        volume_slider.grid(column=6, row=3)
        volume_slider.set(const.DEFAULT_VOLUME)

    def change_volume(self, new_volume):
        self.theremin.adjust_volume(float(new_volume))
