#!/usr/bin/python

import requests
import sys
import json

url = "http://10.144.7.2/api/share/volumes"
key = {'X-AccelStor-API-Key':'4e40139db3e56759fd28ec3f542065eb9048020a'}

session = requests.Session()
session.trust_env = False

#vol = {"size" : 1024, "alias" : "vol9", "type" : "block" }
if len(sys.argv) == 1:
    print "[-] Usage: ./createvol.py <'{\"alias\" : \"vol0\", \"type\" : \"block\", \"size\" : 10240}'>"
    exit()
else:
    vol = json.loads(sys.argv[1])

    response = session.post(url, data=vol, headers=key)
    session.close()

    print response
    print response.content
