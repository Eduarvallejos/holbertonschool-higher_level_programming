#!/usr/bin/python3
"""
Define una clase Rectangle que hereda de BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Representa un rectángulo utilizando BaseGeometry.
    """

    def __init__(self, width, height):
        """Inicializa un nuevo Rectangle.

        Args:
            width (int): El ancho del nuevo Rectangle.
            height (int): La altura del nuevo Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Devuelve el área del rectángulo.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Devuelve la representación de impresión y str() de un Rectangle.
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
