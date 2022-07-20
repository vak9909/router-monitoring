import json
import os
import time
from datetime import datetime
s = "stat\\" + "stat_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
contents = ""

while True: # infinite loop repeating every 10 seconds
    
    os.system("wget -O JSON\model.json http://192.168.1.1/api/model.json")

    with open("JSON\model.json") as json_file:
        data = json.load(json_file)

    f = open(s, "w")
    f.write("[" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "] ")
    f.write("RSRP: " + str(data["wwan"]["signalStrength"]["rsrp"]) + " CellID: " + str(data["wwanadv"]["cellId"]) + " ")
    f.write("CurrentTemp: " + str(data["general"]["devTemperature"]) + " BatteryTemp: " + str(data["power"]["batteryTemperature"]) + "\n" + contents)
    f.close()
    
    # update contents
    f = open(s, "r")
    contents = f.read()
    f.close()
    
    os.system("del JSON\model.json")
    time.sleep(10)


