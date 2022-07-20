import json
import os
import time
from datetime import datetime

while True:
    
    os.system("wget http://192.168.1.1/api/model.json")

    with open("model.json") as json_file:
        data = json.load(json_file)

    file = open("statistics\statistics.txt", "a")
    file.write("[" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "] ")
    file.write("RSRP: " + str(data["wwan"]["signalStrength"]["rsrp"]) + " CellID: " + str(data["wwanadv"]["cellId"]) + " ")
    file.write("CurrentTemp: " + str(data["general"]["devTemperature"]) + " BatteryTemp: " + str(data["power"]["batteryTemperature"]) + "\n")
    file.close()
    
    os.system("del model.json")
    time.sleep(10)

# print(data["general"]["devTemperature"])
# print(data["power"]["batteryTemperature"])

