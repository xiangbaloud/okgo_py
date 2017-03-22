#!/usr/bin/python

import sys
import requests

def usage():
    print('[-] Usage: ./getvolinfo.py <uuid>, if you want to display all vols, use <all>')
    exit(0)

def main():
    url = "http://10.144.7.2/api/share/volumes"
    key = {'X-AccelStor-API-Key':'4e40139db3e56759fd28ec3f542065eb9048020a'}

    if len(sys.argv) > 1:
        argv = str(sys.argv[1])
        if argv == "all":
            url_vol = url
        else:
            vol_uuid = argv
            url_vol = "http://10.144.7.2/api/share/volumes/" + vol_uuid
    else:
        usage()
    
    session = requests.Session()
    session.trust_env = False

    response = session.get(url_vol, headers=key)
    session.close()

    print response
    print response.content

if __name__ == '__main__':
    main() 
