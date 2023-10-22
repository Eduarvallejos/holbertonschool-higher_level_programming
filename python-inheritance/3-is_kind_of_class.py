#!/usr/bin/python3
"""
Se define una funcion llamada is_kind_of_class para verificar la instancia.
"""


def is_kind_of_class(obj, a_class):
    """
    verifica si un objeto es una instancia o una instancia heredada
    de la clase especificada.

    Args:
    obj: El objeto se va a verificar.
    a_class La clase que se va a verificar.

    Returns:
    True si obj es una instancia o una instancia heredada de a_class,
    False en caso comtrario.
    """
    return isinstance(obj, a_class)
