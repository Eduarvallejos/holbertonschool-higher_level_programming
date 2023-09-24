#!/usr/bin/python3
def uppercase(str):
    resultado = ""
    for caracter in str:
        if 'a' <= caracter <= 'z':
            resultado += chr(ord(caracter) - ord('a') + ord('A'))
        else:
            resultado += caracter
    print(resultado)
