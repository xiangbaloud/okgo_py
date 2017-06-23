#!/usr/bin/python

import sys

def josephus(n, skip):
    skip = skip - 1
    idx = skip
    while len(n) > 1:
        print n
        n.pop(idx)
        idx = (idx + skip) % len(n)
    print 'survivor: ', n[0]

def main():
    people = int(sys.argv[1])
    list_a = range(1, people)
    skiper = int(sys.argv[2])
    
    josephus(list_a, skiper)

if __name__ == '__main__':
    main()
