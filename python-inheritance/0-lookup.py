#!/usr/bin/python3
def lookup(obj):
    """
    Utiliza la funcion dir() para obtener una lista de atributos
    y metodos del objeto
    """
    attributes_and_methods = dir(obj)
    return attributes_and_methods
