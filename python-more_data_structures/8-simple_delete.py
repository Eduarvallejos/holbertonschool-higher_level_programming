#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Verificar si la clave existe en el diccionario
    if key in a_dictionary:
        del a_dictionary[key]
        return a_dictionary  # Devolver el diccionario actualizado
