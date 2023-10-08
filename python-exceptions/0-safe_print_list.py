#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element_printed = 0
    try:
        for i in range(x):
            if i < len(my_list):
                print(my_list[i], end='')
                element_printed += 1
    except IndexError:
        pass  # Manejamos la excepcion IndexError si ocurre
    print()  # Agregamos una nueva linea al final
    return element_printed
