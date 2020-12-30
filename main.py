# Python audio transcription from audio file
import speech_recognition as sr
import sys
from os import path
from pydub import AudioSegment
import sphinxbase
import pocketsphinx
from pprint import pprint

#
if __name__ == '__main__':

    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <audio_file>")
    audio_file = sys.argv[1]
    sound = AudioSegment.from_mp3(audio_file)
    sound.export("transcript.wav", format="wav")

    # transcribe audio file
    AUDIO_FILE = "transcript.wav"

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Sphinx
    try:
        result = r.recognize_sphinx(audio)
        pprint(result)
        #print("Sphinx thinks you said: " + )
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

    #print("Transcription: " + r.recognize_google(audio))
