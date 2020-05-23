import numpy
from . import synth_const


# get the frequency of the note indexed at note_i out of n_notes
def get_note_freq(note_i, n_notes):
    return synth_const.MIN_FREQ + (synth_const.MAX_FREQ - synth_const.MIN_FREQ)*note_i/n_notes


# take the given frequency and convert it into an ndarray of samples
def make_note(frequency):
    # make an array of many 1000's of frames, each one with a value of its position in time
    steady_hill = numpy.linspace(0, synth_const.NOTE_LENGTH, synth_const.N_SINGLE_NOTE_FRAMES, False)
    # convert this to a sine wave where each element is sin(position*frequency*2pi)
    single_note_wave = numpy.sin(steady_hill * frequency * 2 * numpy.pi)
    # add this to the list of notes
    return single_note_wave


# take the given sound-like bytes and fix up the amplitude, size, etc
def make_sound(note):
    # turn the note into a numpy array
    sound = numpy.array(note)
    # stretch / shrink the song amplitude-wise
    sound = sound * synth_const.MAX_AMP * (2 ** 15 - 1) / numpy.max(sound)
    # convert to 16 bits
    sound = sound.astype(numpy.int16)
    return sound
