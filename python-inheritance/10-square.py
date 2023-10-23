#!/usr/bin/python3
"""
Define una subclase Rectangle llamada Square.
"""
Rectangle = __import__('9-rectangle').Rectangle

"""
Definición de la clase Square.
"""


class Square(Rectangle):
    """Representa un cuadrado."""

    def __init__(self, size):
        """Inicializa un nuevo cuadrado.

        Args:
            size (int): El tamaño del nuevo cuadrado.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
