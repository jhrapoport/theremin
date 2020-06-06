import tkinter as tk
import const
import Theremin


class Gui:
    def __init__(self):
        self.theremin = Theremin.Theremin(const.ANTENNA_X, const.CANVAS_HEIGHT)
        self.window = tk.Tk()
        self.config()
        self.run()

    def run(self):
        self.window.mainloop()

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
        canvas.bind("<Leave>", self.on_leave)
        self.draw_theremin(canvas)

    def draw_theremin(self, canvas):
        canvas.create_line(const.ANTENNA_X, 10, const.ANTENNA_X, const.CANVAS_HEIGHT - 10, width=4)
        canvas.create_polygon(const.ANTENNA_X + 20, const.CANVAS_HEIGHT - 10,
                              const.ANTENNA_X - 40, const.CANVAS_HEIGHT - 10,
                              const.ANTENNA_X - 30, const.CANVAS_HEIGHT - 30,
                              const.ANTENNA_X + 30, const.CANVAS_HEIGHT - 30)

    def on_motion(self, event):
        distance = const.CANVAS_LENGTH / 2 - abs(const.CANVAS_LENGTH / 2 - event.x)
        height = const.CANVAS_HEIGHT - event.y - 1
        self.theremin.switch_sound(distance, height)

    def on_leave(self, event):
        self.theremin.pause()

    def on_close(self):
        self.theremin.destruct()
        self.window.destroy()

    def add_widgets(self):
        volume_slider = tk.Scale(self.window, command=lambda x: self.change_volume(x))
        volume_slider.config(background="darkgray", from_=0.0, to=1.0, resolution=0.01, length=64)
        volume_slider.config(label="Volume", orient=tk.HORIZONTAL, showvalue=0, sliderlength=15)
        volume_slider.grid(column=6, row=3)
        volume_slider.set(const.DEFAULT_VOLUME)

    def change_volume(self, new_volume):
        self.theremin.adjust_volume(float(new_volume))
