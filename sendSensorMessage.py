import json,httplib, sys

# http://pubsub.pubnub.com/publish/pub-c-db55d0d1-65c7-4814-a2a4-f72278c65812/sub-c-853eef00-65a0-11e5-bba9-02ee2ddab7fe/0/fredEmbedded/0/%22SendSensorsDb%22
text_file = open(sys.path[0]+"/config.json", "r")
username = json.loads(text_file.read())["username"]
text_file.close()

EMBEDDED_CHANNEL = username + "Embedded"
SEND_SENSOR_DB = "SendSensorsDb"
connection = httplib.HTTPConnection('pubsub.pubnub.com')
connection.connect()
url = "/publish/pub-c-db55d0d1-65c7-4814-a2a4-f72278c65812/sub-c-853eef00-65a0-11e5-bba9-02ee2ddab7fe/0/" + EMBEDDED_CHANNEL + "/0/\"" + SEND_SENSOR_DB + "\""
connection.request('GET', "/publish/pub-c-db55d0d1-65c7-4814-a2a4-f72278c65812/sub-c-853eef00-65a0-11e5-bba9-02ee2ddab7fe/0/" + EMBEDDED_CHANNEL + "/0/\"" + SEND_SENSOR_DB + "\"")
results = json.loads(connection.getresponse().read())
print results
