import numpy
from Synth import synth_const


def make_sound(note):
    # turn the note into a numpy array
    sound = numpy.array(note)
    # stretch / shrink the song amplitude-wise
    sound = sound * synth_const.MAX_AMP * (2 ** 15 - 1) / numpy.max(sound)
    # convert to 16 bits
    sound = sound.astype(numpy.int16)
    return sound
