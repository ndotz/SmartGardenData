import json,httplib,urllib,sys
results = ""
sessionToken = sys.argv[1]
# text_file = open("config.json", "r")
# sessionToken = json.loads(text_file.read())["sessionToken"]
# text_file.close()
# sessionToken = "r:C1sCmEtdOha3KI8yS42BI8zvO"
while True: #keep trying until you have internet
    try:
        connection = httplib.HTTPSConnection('api.parse.com', 443)
        connection.connect()
        connection.request('GET', '/1/users/me', '', {
               "X-Parse-Application-Id": "CGoWmZK6uPmAUuldwGcVwOb871lehEClGlGwVTp2",
               "X-Parse-REST-API-Key": "h50pKtIj7oNDqWGoz3zUFhoqKbVdeOrPSosGK0zJ",
               "X-Parse-Session-Token": sessionToken
             })
        user = json.loads(connection.getresponse().read())

        params = urllib.urlencode({"where":json.dumps({
           "user": user["username"],
           "inUse": True
        })})
        connection.request('GET', '/1/classes/Plant?%s' % params, '', {
               "X-Parse-Application-Id": "CGoWmZK6uPmAUuldwGcVwOb871lehEClGlGwVTp2",
               "X-Parse-REST-API-Key": "h50pKtIj7oNDqWGoz3zUFhoqKbVdeOrPSosGK0zJ",
               "X-Parse-Session-Token": sessionToken
             })
        result = json.loads(connection.getresponse().read())
        # print json.dumps({
        #     "userObjectId":user["objectId"],
        #     "plantObjectId":result["results"][0]["objectId"],
        #     "waterAmount":result["results"][0]["waterAmount"],
        #     "harvest": len(result["results"][0]["harvests"]),
        #     "moistureLimit": result["results"][0]["moistureLimit"],
        #     "username": user["username"]
        # })
        print json.dumps([
            user["objectId"],
            result["results"][0]["objectId"],
            result["results"][0]["waterAmount"],
            len(result["results"][0]["harvests"]),
            result["results"][0]["moistureLimit"],
            user["username"]
        ])
        break
    except Exception as e:
        s = str(e)