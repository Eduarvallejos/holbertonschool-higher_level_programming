#!/usr/bin/python3
"""
Esta modulo representa una clase Rectangle.
"""


class Rectangle:
    """
    Este es una clase que define un rectangulo.
    """
    def __init__(self, width=0, height=0):
        """
        Contructor: Inicializa el rectangulo con un ancho y una altura.
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Propiedad para obtener el ancho de un rectangulo.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Propiedad para establecer el ancho de un rectangulo.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Propiedad para obtener la altura de un rectangulo.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Propiedad para establese la altura de una rectangulo.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
