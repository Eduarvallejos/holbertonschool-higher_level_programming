#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}  # Crear un nuevo diccionario vacío
    for key, value in a_dictionary.items():
        new_value = value * 2  # Multiplicar el valor por 2
        # Agregar la clave y el valor actualizado al nuevo diccionario
        new_dictionary[key] = new_value
    return new_dictionary  # Devolver el nuevo diccionario
