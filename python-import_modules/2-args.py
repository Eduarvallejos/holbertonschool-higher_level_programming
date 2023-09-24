#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    num_argumentos = len(argv) - 1
    argumentos = argv[1:]

    if num_argumentos == 0:
        print("0 arguments.")
    else:
        print(f"{num_argumentos} argument{'s' if num_argumentos > 1 else ''}:")
        for i, arg in enumerate(argumentos, start=1):
            print(f"{i}: {arg}")
