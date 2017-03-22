#!/usr/bin/python

import sys
import requests

def usage():
    print('[-] Usage: ./getiscsiinfo.py <uuid>, if you want to display all targets, use <all>')
    exit(0)

def main():
    url = "http://10.144.7.2/api/share/iscsi/targets/"
    key = {'X-AccelStor-API-Key':'4e40139db3e56759fd28ec3f542065eb9048020a'}

    if len(sys.argv) > 1:
        argv = str(sys.argv[1])
        if argv == "all":
            url_iscsi = url
        else:
            target_uuid = argv
            url_iscsi = "http://10.144.7.2/api/share/iscsi/targets/" + target_uuid
    else:
        usage()

    session = requests.Session()
    session.trust_env = False

    response = session.get(url_iscsi, headers=key)
    session.close()

    print response
    print response.content

if __name__ == '__main__':
    main()


