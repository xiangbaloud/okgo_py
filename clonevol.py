#!/usr/bin/python

import requests
import sys
import json

url = "http://10.144.7.2/api/share/volumes/"
key = {'X-AccelStor-API-Key':'4e40139db3e56759fd28ec3f542065eb9048020a'}

session = requests.Session()
session.trust_env = False

if len(sys.argv) == 1:
    print "[-] Usage: ./clonevol.py <uuid> <'{\"alias\" : \"vol0\"}'>"
    exit()
else:
    vol_id = str(sys.argv[1])
    r_url = url + vol_id
    new_vol = json.loads(sys.argv[2])

    response = session.post(r_url, data=new_vol, headers=key)
    session.close()

    print response
    print response.content
