import json,httplib, sys
print "py script sending"
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/classes/SensorData', json.dumps({
        "plant": sys.argv[6],
        "temperature":float(sys.argv[1]),
        "humidity":float(sys.argv[2]),
        "moisture":float(sys.argv[3]),
        "light":float(sys.argv[4]),
        "water":float(sys.argv[7]),
        "harvest":int(sys.argv[8]),
        "ACL":  {
            sys.argv[5]: {
                "read": True,
                "write": True
            },
            "*":{
                "read":True
            }
        }
     }), {
       "X-Parse-Application-Id": "CGoWmZK6uPmAUuldwGcVwOb871lehEClGlGwVTp2",
       "X-Parse-REST-API-Key": "h50pKtIj7oNDqWGoz3zUFhoqKbVdeOrPSosGK0zJ",
       "Content-Type": "application/json"
     })
results = json.loads(connection.getresponse().read())
print results