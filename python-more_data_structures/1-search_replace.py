#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Creamos una nueva lista para almacenar el resultado
    new_list = []
    # Iteramos a través de los elementos de la lista original
    for item in my_list:
        # Si el elemento actual es igual al elemento a buscar, lo reemplazamos
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)

        return new_list
