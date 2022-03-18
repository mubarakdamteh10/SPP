import datetime
import random
from speechtext import *
from status import *

def call_in_function(sound):
    if sound == "water":
        print("show water status")
        return speechtext("show water status")
        
    elif sound == "sunlight" :
        print("open sunlight")
        return speechtext("open sunlight")
    elif sound == "status":
        print("show status")
        return speechtext("show status")
    elif sound == "turning on water":
        return speechtext("waterring now")
    elif sound == "turn on light":
        print("turning on the light")
        return speechtext("turning on the light")
    elif Sound == "status":
        result = status()
        print("showing status")
        return speechtext("showing status")
    
# def call_water(command):
#     if command == "turn on water":
#         return "I'm waterring"
    
# def call_light(command):
#     if command == "turn on light":
#         return "I'm turn on the light"
    
# def call_stautus(command):
#     if command == "status":
#         return "showing status"