import pyaudio
import speech_recognition as sr
from callfunction import *

# print(sr.Microphone.list_microphone_names())

mic = sr.Microphone(1)
recog = sr.Recognizer()
with mic as source:
    while True:
        print("say something !")
        audio = recog.listen(source,timeout=5.0)
        try:
            voice = recog.recognize_google(audio,language='th')
            print(voice)
            print(call_in_function(voice))
            print("New Command")
        except:
            continue
        print("out")
        