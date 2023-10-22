#!/usr/bin/python3
"""
Define una funcion llamada lookup que obtiene una lista de atributos
y metodos de un objeto.
"""


def lookup(obj):
    """
    Utiliza la funcion dir() para obtener una lista de atributos
    y metodos del objeto.
    -param obj: El objeto del que se desea obtener los atributos y metodos.
    -return: Una lista que contienen los atributos y metodos del objeto.
    """
    list = dir(obj)
    return list
