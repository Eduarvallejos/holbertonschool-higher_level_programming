#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Verificar si la clave existe en el diccionario
    if key in a_dictionary:
        # Si la clave existe, reemplazar el valor
        a_dictionary[key] = value
    else:
        # Si la clave no existe, agregar una nueva entrada
        a_dictionary[key] = value
