from gtts import gTTS
from playsound import  playsound


def speechtext(text):
    t = text
    mytext=t
    language='en'
    myobj=gTTS(text=mytext,lang=language,slow=False)
    myobj.save("welcome1.mp3")
    playsound("welcome1.mp3")