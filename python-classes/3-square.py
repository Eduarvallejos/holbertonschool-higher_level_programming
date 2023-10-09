#!/usr/bin/python3
"""
Este modulo representa una clase square.
"""


class Square:
    """
    este es una clase que define un cuadrado.
    """
    def __init__(self, size=0):
        """
        Inicializa una instancia de Square con un tamaño opcional dado.

        Args:
            size (int, opcional): El tamaño del cuadrado
            (verificación de tipo y valor).
                El valor predeterminado es 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calcula y devuelve el área del cuadrado.

        Returns:
            int: El área del cuadrado (lado * lado).
        """
        return self.__size * self.__size
