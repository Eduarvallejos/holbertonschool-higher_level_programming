#!/usr/bin/python3
output = ""
for number in range(100):
    output += "{:02d}{}".format(number,', ' if number < 99 else '\n')
print(output, end='')
