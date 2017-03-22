#!/usr/bin/python

import requests
import json
import sys

url = "http://10.144.7.2/api/share/iscsi/targets"
key = {'X-AccelStor-API-Key':'4e40139db3e56759fd28ec3f542065eb9048020a'}

session = requests.Session()
session.trust_env = False

#vol = {"size" : 1024, "alias" : "vol9", "type" : "block" }
if len(sys.argv) == 1:
    print "[-] Usage: ./createvol.py <'{\"identifier\" : \"san01\"}'>"
    exit()
else:
    iscsi_target = json.loads(sys.argv[1])

    response = session.post(url, data=iscsi_target, headers=key)
    session.close()

    print response
    print response.content
