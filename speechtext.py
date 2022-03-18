from gtts import gTTS
from playsound import  playsound


def speechtext(text):
    mytext=text
    language='en'
    myobj=gTTS(text=mytext,lang=language,slow=False)
    myobj.save("welcome1.mp3")
    playsound("welcome1.mp3")
    
# mytext=text
# language='th'
# myobj=gTTS(text=mytext,lang=language,slow=False)
# myobj.save("welcome1.mp3")
# playsound("welcome1.mp3")