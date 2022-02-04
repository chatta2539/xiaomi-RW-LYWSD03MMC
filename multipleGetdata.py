import json
from lywsd03mmc import Lywsd03mmcClient

import paho.mqtt.client as mqtt
host = "broker.mqttdashboard.com"
port = 8000
client = mqtt.Client()
client.connect(host)

my_json_string = """{
  "xiaomi": [
    {
      "id": 1,
      "name": "Raeh",
      "mac": "A4:C1:38:A7:3A:5C"
    },
    {
      "id": 2,
      "name": "No.1",
      "mac": "A4:C1:38:AB:6E:80"
    },
    {
      "id": 3,
      "name": "No.2",
      "mac": "A4:C1:38:60:D6:5B"
    },
    {
      "id": 4,
      "name": "No.3",
      "mac": "A4:C1:38:C4:64:BA"
    }
  ]
}"""
devices = json.loads(my_json_string)

def getTemplog(selectDevice):
   print(devices["xiaomi"][selectDevice])
   try:
      data = Lywsd03mmcClient(devices["xiaomi"][selectDevice]["mac"]).data
      test = {
            "DeviceName" : devices["xiaomi"][selectDevice]["name"],
            "Temperature" : float(data.temperature),
            "Humidity" : float(data.humidity),
            "Battery" : float(data.battery),
            "ConnectionStatus" : "OK"
            }
      tmp = json.dumps(test)

   except Exception as e:
      print(e)
      test = {
            "DeviceName" : devices["xiaomi"][selectDevice]["name"],
            "Temperature" : None,
            "Humidity" : None,
            "Battery" : None,
            "ConnectionStatus" : str(e)
            }
      tmp = json.dumps(test)
      
   return tmp

for i in range(len(devices["xiaomi"])):
   respond = getTemplog(i)
   print(respond)
   client.publish("TEST/Raeh",respond)
   
