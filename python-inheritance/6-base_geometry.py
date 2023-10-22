#!/usr/bin/python3
"""
definimos una funcion BaseGeometry
"""


class BaseGeometry:
    """
    BaseGemotry nos servira como una clase base para operaciones de
    geometria
    """
    def area(self):
        """
        Este metodo lanza una excepcion indicando que area() no
        esta implimentado.
        """
        raise Exception("area() is not implemented")
