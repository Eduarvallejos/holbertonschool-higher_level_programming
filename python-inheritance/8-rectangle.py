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
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    La clase rectangle hereda a Basegeometry.
    """
    def __init__(self, width, height):
        """
        Inicializa los atributos privados de ancho y alto.
        """
        self.__width = width
        self.__height = height
        """Llama al método integer_validator de la clase base para validar
        si el ancho y el alto son enteros.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
