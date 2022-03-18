from speechtext import *

def status():
    light_value = NULL
    water_value = NULL
    watering_time = 3000000000

    if light_value != 0 and water_value != 0:
        if light_value > 100 :
            print("bring tactus to another place here is too warm")
            return speechtext("bring tactus to another place here is too warm")
        elif light_value <= 50:
            print("the tactus need more sun light ")
        elif water_value > 50 :
            print("there is too much water for taccus now")
            return speechtext("there is too much water for taccus now")
        elif water_value <= 15 :
            print("the tactus need more water")
            return speechtext("the tactus need more water")
        elif water_value > 50 and light_value <= 50 :
            print("")
