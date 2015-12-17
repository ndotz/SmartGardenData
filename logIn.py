import json,httplib,urllib,sys
connection = httplib.HTTPSConnection('api.parse.com', 443)
params = urllib.urlencode({"username":sys.argv[1],"password":sys.argv[2]})
connection.connect()
connection.request('GET', '/1/login?%s' % params, '', {
       "X-Parse-Application-Id": "CGoWmZK6uPmAUuldwGcVwOb871lehEClGlGwVTp2",
       "X-Parse-REST-API-Key": "h50pKtIj7oNDqWGoz3zUFhoqKbVdeOrPSosGK0zJ",
       "X-Parse-Revocable-Session": "1"
     })
user = json.loads(connection.getresponse().read())

text_file = open("config.json", "w")
text_file.write(json.dumps({
    "sessionToken":user["sessionToken"],
    "username":sys.argv[1]
}))
text_file.close()
print "done"