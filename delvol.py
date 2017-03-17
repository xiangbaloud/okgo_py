#!/usr/bin/python

import requests
import sys

url = "http://10.144.7.2/api/share/volumes"
key = {'X-AccelStor-API-Key':'4e40139db3e56759fd28ec3f542065eb9048020a'}

vol_uuid = "a86488b0-4178-422f-bfbb-dce9d170b2b5"
if len(sys.argv) == 1:
    print "[-] Usage: ./delvol.py <uuid>"
    exit()
else:
    vol_uuid = str(sys.argv[1])
    url_vol = "http://10.144.7.2/api/share/volumes/" + vol_uuid

    session = requests.Session()
    session.trust_env = False

    response = session.delete(url_vol, headers=key)
    session.close()

    print response
    print response.content
