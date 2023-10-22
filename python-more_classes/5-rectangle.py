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
        Propiedad para establecer el ancho de un rectangulo con verificacion.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
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
        Propiedad para establecer la altura de un rectangulo con verificacion.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Propiedad para calcular el area de un rectangulo.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Propiedad para calcular el perimetro de un rectangulo.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Metodo para generar una representacion en forma de cadena del
        rectangulo con caracteres #.
        Si el ancho o la altura es igual a 0, se devuelve una cadena vacia.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect_str = ""
            for _ in range(self.__height):
                rect_str += "#" * self.__width + "\n"
            return rect_str.rstrip()

    def __repr__(self):
        """
        Devuelve una representacion en cadena que permite recrear
        esta instancia de la clase.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Metodo especial de eliminacion (__del__):
        Se ejecuta cuando un objeto esta a punto de ser destruido.
        Imprime un mensaje de despedida.
        """
        print("Bye rectangle...")
