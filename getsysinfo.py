#!/usr/bin/python

import requests

url = "http://10.144.7.2/api/system/info"
key = {'X-AccelStor-API-Key':'4e40139db3e56759fd28ec3f542065eb9048020a'}

session = requests.Session()
session.trust_env = False

response = session.get(url, headers=key)
session.close()

print response
print response.content
