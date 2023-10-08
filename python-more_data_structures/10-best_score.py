#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    # Inicialmente, no se ha encontrado ninguna clave
    max_key = None
    # Inicialmente, el valor máximo es negativo infinito
    max_value = float("-inf")
    for key, value in a_dictionary.items():
        if isinstance(value, int) and value > max_value:
            max_key = key
            max_value = value

    return max_key
