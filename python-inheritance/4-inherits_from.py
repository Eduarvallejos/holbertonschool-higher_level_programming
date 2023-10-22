#!/usr/bin/python3
"""
Se define la funcion inherits_from para validar la instancia.
"""


def inherits_from(obj, a_class):
    """
    Verifica si un objeto es una instancia de una clase que heredó
    (directa o indirectamente) de la clase especificada.

    Args:
    obj: El objeto que se va a verificar.
    a_class: La clase contra la que se va a verificar.

    Returns:
    True si el objeto es una instancia de una clase que heredó de a_class;
    False en caso contrario.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
