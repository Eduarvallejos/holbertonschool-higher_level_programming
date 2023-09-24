#!/usr/bin/python3
for letra in range(ord('a'), ord('z') + 1):
    if chr(letra) not in ['e', 'q']:
        print(chr(letra), end='')
