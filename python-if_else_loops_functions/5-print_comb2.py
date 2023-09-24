#!/usr/bin/python3
output = ""
for number in range(100):
        output += "{}{}".format(number,', ' if number < 99 else '\n')
print(output, end='')
