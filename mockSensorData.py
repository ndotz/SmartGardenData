# Program to generate mock data containing an object for every hour period from the last 10 days.
# The program writes a json file that is used in parse.com's import feature. We use this instead of their
# REST API because createdAt is normally generated automatically and can't be altered through their REST API.
import json,httplib,urllib,time,datetime, random, iso8601
from pip._vendor.pkg_resources.tests.test_pkg_resources import timestamp

nowInMilliseconds = int(round(time.time() * 1000)) # Dates as milliseconds since 1970
hourInMilliseconds = 3600000
tenDaysInMilliseconds = 864000000

mockSensorInfo = [
    {
        'createdAt':datetime.datetime.fromtimestamp(mocTime/1000.0).isoformat(),
        'updatedAt':datetime.datetime.fromtimestamp(mocTime/1000.0).isoformat(),
        'moisture':random.randint(0,100),
        'humidity':random.randint(0,100),
        'temperature':random.randint(0,100),
        'light':random.randint(0,100),
        'harvest': 0,
        'water':0.1,
        "plant":"VPDBST44g6"
    } for mocTime in range(nowInMilliseconds - tenDaysInMilliseconds, nowInMilliseconds, hourInMilliseconds)]    #every hour of the last ten days

text_file = open(".\SensorData.json", "w")
text_file.write(json.dumps({
    "results":mockSensorInfo
}))
text_file.close()

print mockSensorInfo