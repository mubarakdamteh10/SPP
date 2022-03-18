import pyaudio
import speech_recognition as sr
from callfunction import *

# print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(1)
recog = sr.Recognizer()
with mic as source:
    while True:
        audio = recog.listen(source)
        try:
            voice = recog.recognize_google(audio,language='en')
            print(voice)
            print(call_in_function(voice))
            print("New Command")
        except:
            continue
        