#!/usr/bin/python3
"""
definimos una funcion BaseGeometry
"""


class BaseGeometry:
    def area(self):
        """
        Este metodo lanza una excepcion indicando que area() no
        esta implimentado.
        """
        raise Exception("area() is not implemented")
