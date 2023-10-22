#!/usr/bin/python3
"""
Se define una funcuin llamada is_same_class que verifica si un objeto
es exactamente una instancia de una clase especificada.
"""


def is_same_class(obj, a_class):
    """
    Compara la clase del objeto (type(obj))
    con la clase especificada (a_class).
    - Si son iguales, devuelve True; de lo contrario,
    devuelve False.
    """
    return type(obj) is a_class
