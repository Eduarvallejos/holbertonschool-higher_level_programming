#!/usr/bin/python3
output = ''
for letra in range(ord('a'), ord('z') + 1):
    if chr(letra) not in ['e', 'q']:
        output += chr(letra)

print("{}".format(output), end= '')
