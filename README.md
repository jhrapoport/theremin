
### Jesse Rapoport -- jhr@pdx.edu -- "Soft Keyboard Group"

# CS 410P Final Theremin Project
## What this program is and does

This is a theremin program! Essentially, you can scroll your mouse around a given area, with an illustration of a theremin in the middle, and then it will make sounds like a theremin as you do so. Moving your mouse closer to the theremin will raise the frequency, and moving it higher will increase the amplitude/volume.

Additional features include a volume slider, user-controlled minimum/maximum frequencies and tempo, a 4/4 metronome, and a play-along guide for the song of your choice.

## Testing

For user-input on the frequencies and tempo, it initially would give errors when given non-numeric values. I fixed that, and then later I also stopped errors from negative numbers. The test for this was that it would keep running without error when given these inputs, which is what happened. 

As is described in the next section, I tested the audio quite a lot using Audio Recorder and Audacity. Audio Recorder allowed me to capture exactly what was coming out of my program, and Audacity allowed me to look at each pulse in the sound files. Doing this allowed me to find all of my errors pretty easily. 

Before using Audio Recorder/Audacity, I was hearing bad sounds and not knowing why. However, looking at the sound files, it became very clear exactly what was happening. I could see that the sine waves were switching over at random points, making disrupted noises. Once I tried to fix this, I saw the issue there as well, which was that a sine wave going up would then match up at the same height with a sine wave going down, which sounded just as bad. I go more into this in the following section. I also have the audio files in question, but the assignment requirements sound to me like I shouldn't include them; let me know if you'd like me to send them your way so you can hear the vast improvement in sound.

One more test I did was on the metronome. I used my phone's stopwatch to ensure that it was keeping the number of beats it said it was. I tried this for one minute for 30bpm, 60pm, and 90bpm, and it worked as expectedly.


## Satisfaction
Overall, the program worked much better than I expected it to. I wrote everything from complete scratch, so I didn't expect it to work very well.

The first major issue was that the sound was not clean. I looked at the audio in Audacity, and found that the sine waves, when switching, were causing noises because the instantaneous sine values between waves would be so misaligned. Without Googling or anything, I just made a simple fix to match up the sine waves: checking whether the instantaneous value at the end of the prior sine wave was going up or down, and getting its height. Then, offsetting the next sine wave to start at the same height, going the same direction, up or down, as the wave prior.

This was 90% effective. The sound was truly horrible before the change, so after that it sounded clean and beautiful. However, there were still occasional noises, clear disruptions of the sine waves. I looked in Audacity again, and found that my algorithm wasn't perfect. Sometimes instantaneous values would be above or below their neighbor when they shouldn't be, causing my calculation of it going up or down to be incorrect. Worse, when a value was at the top or bottom of a sine wave, it would be very hard mathematically to match up with, as their paths might never quite cross, which was what we were waiting for to find a match.

I tried numerous solutions, and none of them worked well. The best one I found made it up to 95% effective, I'd say: now, if it doesn't find a good match, it just looks for the closest height, ignoring up/downness. This still causes some bad sounds, but it seems to cut most of them out.

I'm very satisfied with the appearance of the program and some of the functionality. It was fun making a metronome. It was also fun generating sounds from scratch, and even moreso it was fun calculating note frequencies purely from the starting value of A4 = 440.0 Hz. The most fun and satisfying thing, though, was giving the ability to insert a song and allow the user to play along with it. This took a lot of math, but it turned out pretty nicely I think.

One thing I don't like right now is that the metronome does not sound good when you have the song playing with it. The audio is fine, but the rhythm is off. I would have to differentiate between metronome beats and note length to do that, which I don't have time to do tonight. That's something I would add, as well as a piano feature that shows you all of the keys displayed at once. 

# Sources
The metronome sounds came from these websites, under the Creative Commons  0 License:
https://freesound.org/people/MattiaGiovanetti/sounds/475901/
https://freesound.org/people/Druminfected/sounds/250552/

# Dependencies
To run this program, in addition to the Python standard library, you need to have the following Python packages installed: simpleaudio, numpy, and sounddevice.

# Usage
Using Python 3, simply run main.py. In the Linux terminal, this would just be the  following command:  <code> python3 ./main.py </code>

If you want to play a different song than the example in "song_notes.csv", you need to make a CSV file in the same format as that one. That is, giving one beat to each note name, and separating via commas in one long line. You can use that filename given, or change its value in the variable <code>SONG_FILE_NAME</code> in const.py.

One extra note: if you want to change the values in the text boxes, make sure to press return after changing the value.