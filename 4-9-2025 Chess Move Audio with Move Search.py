'''
Put intro here

Credits to
https://realpython.com/playing-and-recording-sound-python/
https://github.com/openai/whisper?tab=readme-ov-file
https://ffmpeg.org/ffmpeg.html#Trancoding

and Bing Chat AI for answering some syntax queries and member function explanations
'''

import sounddevice
from scipy.io.wavfile import write

import subprocess
import os

import whisper

def record_audio(duration, filename = "sound.wav"):
    sample_rate = 44100 #standard value in Hz

    my_recording = sounddevice.rec(int(duration * sample_rate), samplerate = sample_rate, channels = 2) #a numpy array of recorded values
    sounddevice.wait() #waits for recording to finish

    #filename2 = "\"" + os.curdir + "/" + filename + "\""
    #like whisper, sounddevice isn't liking quotation marks and os.curdir
    filename2 = os.curdir + "/" + filename

    write(filename2, sample_rate, my_recording)

def transcode_audio(input = "sound.wav", output = "sound.mp3"):
    my_cmd = "ffmpeg -i \"" + os.curdir + "/" + input + "\" \"" + os.curdir + "/" + output + "\" -y"
    #-y is to overwrite any existing file with os.curdir + /sound.mp3 name

    subprocess.check_call(
        my_cmd, shell=True
    )

def transcribe_audio(input = "sound.mp3"):
    model = whisper.load_model("tiny.en")

    #filepath = "\"" + os.curdir + "/" + input + "\""
    #so, for some reason whisper doesn't like "./sound.mp3" . . . it doesn't want the quotation marks when you use "."
    filepath = os.curdir + "/" + input

    result = model.transcribe(filepath)
    #print(result["text"])

    return result["text"]

def detect_audio():
    sample_rate = 44100
    duration = 2
    threshold = 0.5

    print("Please Make Noise")

    my_recording = sounddevice.rec(int(duration * sample_rate), samplerate = sample_rate, channels = 2) #a numpy array of recorded values
    sounddevice.wait() #waits for recording to finish

    #print(my_recording.max())
    #print(my_recording.min())
    #print(my_recording.mean())

    if my_recording.max() > threshold:
        return True
    else:
        return False

'''main program here'''

while True:
    proceed = detect_audio()

    if proceed:
        print("speak move")
        record_audio(7)
        transcode_audio()
        output = transcribe_audio()

        print(output)



'''
#main program here
print("speak")

record_audio(5)

print("recording ended")

transcode_audio()
output = transcribe_audio()
#it seems like the deciphering works best if you use a format like "move xy to ab"

print(output)
'''



