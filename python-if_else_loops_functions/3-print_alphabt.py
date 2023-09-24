#!/usr/bin/python3
alphabet = ''.join([chr(letra) for letra in range(ord('a'), ord('z') + 1) if chr(letra) not in 'qe'])
formatted_alphabet = "{}".format(alphabet)
print(formatted_alphabet, end='')
