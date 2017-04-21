#!/usr/bin/python
import sys
import os

def usage():
    print('[-] Usage: python check_file.py <filename1> ... <filenameN>')
    exit(0)

def readf(filename):
    with open(filename, 'r') as f:
        line = f.read()
        print(line)

def main():
    if len(sys.argv) >= 2:
        filenames = sys.argv[1:]
        for filename in filenames:
            if not os.path.isfile(filename):			
                print ('[-] ' + filename + ' does not exist')
                filenames.remove(filename)			
                continue
            if not os.access(filename, os.R_OK):	        
                print ('[-] ' + filename + ' access denied')
                filenames.remove(filename)			
                continue
    else:
        usage()

    for filename in filenames:
        print ('[+] Reading from : ' + filename)
        readf(filename)

if __name__ == '__main__':
    main()
