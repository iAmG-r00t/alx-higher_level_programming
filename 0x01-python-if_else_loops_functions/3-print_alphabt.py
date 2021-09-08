#!/usr/bin/python3
for c in range(ord('a'), ord('z')+1):
    if c is not (ord('q')) and c is not (ord('e')):
        print('{}'.format(chr(c)), end='')
