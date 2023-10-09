#!/usr/bin/python3
"""
Este modulo representa una clase square
"""


class Square:
    def __init__(self, size):
        """
        Inicializa una instancia de Square con un tamaño dado.

        Args:
            size: El tamaño del cuadrado (sin verificación de tipo o valor).
        """
        self.__size = size
