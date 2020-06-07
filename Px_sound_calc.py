import const


class Px_sound_calc:
    def __init__(self):
        self.min_freq = const.MIN_FREQ
        self.max_freq = const.MAX_FREQ
        self.max_amp = const.MAX_AMP
        self.width = const.CANVAS_WIDTH
        self.height = const.CANVAS_HEIGHT
        self.volume = const.DEFAULT_VOLUME

    def get_freq(self, x_px):
        half_width = self.width / 2
        distance = half_width - abs(half_width - x_px)
        return self.min_freq + (self.max_freq - self.min_freq) * distance / half_width

    def get_amp(self, y_px):
        reverse_y = self.height - y_px - 1
        return self.volume * self.max_amp * reverse_y / self.height

    def adjust_volume(self, new_volume):
        self.volume = new_volume
