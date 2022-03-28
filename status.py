from speechtext import *
from random import *
from playsound import  playsound


def checking():
    w = water_status()
    l = light_status()
    if l != "" and w != "":
        if l == True:
            speechtext("lighting on")
        elif w == True:
            speechtext("watering on")
        elif l == False:
            speechtext("lighting off")
        elif w == False:
            speechtext("watering off")
    else:
        speechtext("No status")


def light_status():
    status = [True,False]
    light_value = sample(status,1)
    print(light_value)

def water_status():
    status = [True,False]
    water_value = sample(status,1)
    print(water_value)
