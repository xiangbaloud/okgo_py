#!/usr/bin/python
import sys

class FileReader(object):
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__ (self):
        self.file = open(self.filename, 'r')
        return self.file
    
    def __exit__(self, type, msg, traceback):
        if type:
            print(msg)
        self.file.close()
        return False

f = sys.argv[1]

with FileReader(f) as file:
    for line in file:
        print line
