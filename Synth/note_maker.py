import numpy
from Synth import synth_const

# take the given frequency and convert it into an ndarray of samples
def make_note(frequency):
    # make an array of many 1000's of frames, each one with a value of its position in time
    steady_hill = numpy.linspace(0, synth_const.NOTE_LENGTH, synth_const.N_SINGLE_NOTE_FRAMES, False)
    # convert this to a sine wave where each element is sin(position*frequency*2pi)
    single_note_wave = numpy.sin(steady_hill * frequency * 2 * numpy.pi)
    # add this to the list of notes
    return single_note_wave
