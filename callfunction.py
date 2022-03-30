import datetime
import random
from speechtext import *
from status import display_value

def call_in_function(sound):
    if sound == "water":
        print("show water status")
        return speechtext("show water status")
    elif sound == "แสงแดด" :
        print("open sunlight")
        return speechtext("open sunlight")
    elif sound == "ดูสถานะ":
        print("show status",display_value())
        return speechtext("show status")
    elif sound == "รดน้ำ":
        return speechtext("waterring now")
    elif sound == "เปิดแสง":
        print("turning on the light")
        return speechtext("turning on the light")
    else:
        print("out")