import tkinter as tk
import const
import Theremin
import Px_sound_calc
import note_freq_calc
import Metronome


class Gui:
    def __init__(self):
        self.px_sound_calc = Px_sound_calc.Px_sound_calc()
        self.theremin = Theremin.Theremin()
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window)
        self.metronome = Metronome.Metronome()
        self.config()
        self.run()

    def run(self):
        self.window.mainloop()

    def config(self):
        self.config_window()
        self.config_canvas()
        self.add_widgets()

    def config_window(self):
        self.window.configure(background=const.BG_COLOR)
        self.window.title("Theremin")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.resizable(0, 0)

    def config_canvas(self):
        self.canvas.grid(column=0, row=0, columnspan=5, rowspan=5)
        self.canvas.configure(width=const.CANVAS_WIDTH, height=const.CANVAS_HEIGHT,
                              cursor="hand1 black", background=const.CANVAS_COLOR,
                              highlightthickness=0)
        self.canvas.bind("<Motion>", self.on_motion)
        self.canvas.bind("<Leave>", self.on_leave)
        self.draw_theremin()

    def draw_theremin(self):
        self.canvas.create_polygon(const.ANTENNA_X + 25, const.CANVAS_HEIGHT - 10,
                                   const.ANTENNA_X - 35, const.CANVAS_HEIGHT - 10,
                                   const.ANTENNA_X - 25, const.CANVAS_HEIGHT - 30,
                                   const.ANTENNA_X + 35, const.CANVAS_HEIGHT - 30,
                                   fill=const.THEREMIN_BASE)
        self.canvas.create_line(const.ANTENNA_X, 20, const.ANTENNA_X, const.CANVAS_HEIGHT - 20,
                                width=4, fill=const.THEREMIN_ROD)

    def on_motion(self, event):
        freq = self.px_sound_calc.get_freq(event.x)
        amp = self.px_sound_calc.get_amp(event.y)
        self.theremin.switch_sound(freq, amp)

    def on_leave(self, event):
        self.theremin.pause()

    def on_close(self):
        self.theremin.destruct()
        self.metronome.off()
        self.window.destroy()

    def add_widgets(self):
        self.add_volume_slider()
        self.add_freq_controls()
        self.add_metronome()

    def add_volume_slider(self):
        label = tk.Label(self.window, text="Volume:")
        label.grid(column=6, row=0, sticky=tk.E)
        label.config(fg=const.LABEL_FG_COLOR, bg=const.LABEL_BG_COLOR)
        volume_slider = tk.Scale(self.window, command=lambda x: self.change_volume(x))
        volume_slider.config(background=const.SLIDER_COLOR, from_=0.0, to=1.0,
                             resolution=0.01, length=64, orient=tk.HORIZONTAL,
                             showvalue=0, sliderlength=15, borderwidth=0,
                             troughcolor=const.CANVAS_COLOR, highlightthickness=0)
        volume_slider.grid(column=7, row=0)
        volume_slider.set(const.DEFAULT_VOLUME)

    def change_volume(self, new_volume):
        self.px_sound_calc.adjust_volume(float(new_volume))

    def add_metronome(self):
        label = tk.Label(self.window, text="Metronome:")
        label.grid(column=6, row=1, sticky=tk.E)
        label.config(fg=const.LABEL_FG_COLOR, bg=const.LABEL_BG_COLOR)
        button = tk.Button(self.window)
        button.config(command=lambda: self.on_metronome(button), borderwidth=2, highlightthickness=0,
                      background=const.BUTTON_OFF, activebackground=const.BUTTON_OFF_H)
        button.grid(column=7, row=1)

    def on_metronome(self, button):
        # switch metronome on/off, and change button color accordingly
        if self.metronome.switch():
            button.config(background=const.BUTTON_ON, activebackground=const.BUTTON_ON_H)
        else:
            button.config(background=const.BUTTON_OFF, activebackground=const.BUTTON_OFF_H)

    def add_freq_controls(self):
        label = tk.Label(self.window, text="Min. frequency:")
        label.grid(column=6, row=2, sticky=tk.E)
        label.config(fg=const.LABEL_FG_COLOR, bg=const.LABEL_BG_COLOR)
        min_freq_control = tk.Entry(self.window)
        min_freq_control.config(width=7, highlightthickness=0, borderwidth=0,
                                fg=const.LABEL_BG_COLOR, bg=const.LABEL_FG_COLOR)
        min_freq_control.grid(column=7, row=2)
        min_freq_control.insert(0, const.MIN_FREQ)
        min_freq_control.bind('<Return>', lambda x: self.change_min_freq(min_freq_control.get()))

        label2 = tk.Label(self.window, text="Max. frequency:")
        label2.grid(column=6, row=3, sticky=tk.E)
        label2.config(fg=const.LABEL_FG_COLOR, bg=const.LABEL_BG_COLOR)
        max_freq_control = tk.Entry(self.window)
        max_freq_control.config(width=7, highlightthickness=0, borderwidth=0,
                                fg=const.LABEL_BG_COLOR, bg = const.LABEL_FG_COLOR)
        max_freq_control.grid(column=7, row=3)
        max_freq_control.insert(0, const.MAX_FREQ)
        max_freq_control.bind('<Return>', lambda x: self.change_max_freq(max_freq_control.get()))

    def change_min_freq(self, min_freq):
        try:
            self.px_sound_calc.min_freq = float(min_freq)
        except ValueError:
            return

    def change_max_freq(self, max_freq):
        try:
            self.px_sound_calc.max_freq = float(max_freq)
        except ValueError:
            return

    def draw_line(self, note_name):
        freq = note_freq_calc.get_freq(note_name)
        x_px = self.px_sound_calc.get_px_x(freq)
        self.canvas.create_line(x_px, 10, x_px, const.CANVAS_HEIGHT - 10, width=4, fill=const.NOTE_COLOR)

