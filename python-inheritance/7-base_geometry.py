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

    def integer_validator(self, name, value):
        """
        Verifica si 'value' es una entero y si e mayor o igual que 0,
        Lanzando excepciones si no cumplen con los requisitos.

        Args:
        name (str): El nombre del valor que se esta validando.
        value (int): El valor a ser validado.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
