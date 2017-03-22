#!/usr/bin/python

import requests
import sys
import json

url = "http://10.144.7.2/api/share/iscsi/targets/"
key = {'X-AccelStor-API-Key':'4e40139db3e56759fd28ec3f542065eb9048020a'}

if len(sys.argv) == 1:
    print "[-] Usage: ./createvol.py <target_uuid> <'{\"alias\" : \"vol01\", \"id\" : 0, \"iomode\" : \"wt\"}'>"
    exit()
else:
    iscsi_uuid = str(sys.argv[1])   
    url_lun = url + iscsi_uuid + "/luns"

    session = requests.Session()
    session.trust_env = False
     
    iscsi_target_lun = json.loads(sys.argv[2])

    response = session.post(url_lun, data=iscsi_target_lun, headers=key)
    session.close()

    print response
    print response.content

