from influxdb import InfluxDBClient
from lywsd03mmc import Lywsd03mmcClient
xiaomiTemp = Lywsd03mmcClient("A4:C1:38:A7:3A:5C")

data = xiaomiTemp.data
print('Temperature: ' + str(data.temperature))
print('Humidity: ' + str(data.humidity))
print('Battery: ' + str(data.battery))
print('Display units: ' + xiaomiTemp.units)

loginEvents = [{"measurement": "xiaomiTemp",

        "tags": 
            {
            "unit": xiaomiTemp.units
            },
        "fields":
            {
                "temperature": data.temperature,
                "humidity": data.humidity,
                "Battery": data.battery
            }
}]

dbClient = InfluxDBClient(host='127.0.0.1', port=8086, database='raehdb')



# dbClient.write_points(loginEvents)
# print(loginEvents)
# loginRecords = dbClient.query('select * from xiaomiTemp;')
# print(loginRecords)