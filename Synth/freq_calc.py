from Synth import synth_const


# calculate the frequency of the note requested
def get_freq(note_name, steps_up=0):
    our_letter = note_name[:-1]
    our_freq = synth_const.BASE_FREQUENCY
    position = -1
    for i, general_note in enumerate(synth_const.NOTES):
        position = i
        if our_letter == general_note:
            break
        # if that wasn't it, go up a note here
        our_freq *= 2**(1/12)
    difference = int(note_name[-1]) - int(synth_const.BASE_NOTE[-1])
    # octave changes between b and c, so adjust for that
    if position >= synth_const.OCTAVE_DIVIDER:
        difference -= 1
    if difference == 0:
        return our_freq
    # go up in octaves if needed
    if difference > 0:
        for i in range(difference):
            our_freq *= 2
    # go down in octaves if needed
    if difference < 0:
        for i in range(difference*-1):
            our_freq /= 2
    # go up/down however many steps requested from the initial note
    return our_freq*2**(steps_up/12)
