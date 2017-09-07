#!/usr/bin/python3

import socket
import subprocess
import sys

class host(object):
    def __init__(self, hostname):
        self.hostname = hostname

    def get_host_info(self):
        ip = socket.gethostbyname(hostname)
        return self.hostname + "(" + str(ip) + ")"

    def get_host_status(self):
        ip_address = socket.gethostbyname(hostname)
        response = subprocess.call(["ping", "-c", "3", ip_address], stdout=subprocess.PIPE)
        if response == 0:
            pingstatus = "is up"
        else:
            pingstatus = "is down"
        return str(pingstatus)

if len(sys.argv) > 1:
    hostname = str(sys.argv[1])
    msg = host(hostname).get_host_info() + " " + host(hostname).get_host_status()
    print(msg)
else:
    print("need host arguments")
    exit(0)
