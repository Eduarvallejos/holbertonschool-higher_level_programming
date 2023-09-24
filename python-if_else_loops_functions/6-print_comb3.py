#!/usr/bin/python3
output = ""
for d1 in range(10):
    for d2 in range(d1 + 1, 10):
        output += "{:02d}, ".format(d1 * 10 + d2)

output = output.rstrip(', ')
print(output)
