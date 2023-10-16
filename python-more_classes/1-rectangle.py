#!/usr/bin/python3
"""
Este modulo representa una clase rectangle.
"""


class Rectangle:
    """
    Este es una clase que define un rectangulo.
    """
    def __init__(self, width=0, height=0):
        """
        Constructor: Inicializa el rectangulo con un ancho y una altura.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Propiedad para obtener el ancho de un rectangulo.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Propiedad para establecer el ancho de un rectangulo con verificacion.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        return self.__width

    @property
    def height(self):
        """
        Propiedad para obtener la altura de un rectangulo.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Propiedad para establecer la altura de un rectangulo con verificacion.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        return self.__height
