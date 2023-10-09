#!/usr/bin/python3
"""
Este modulo representa una clase square.
"""


class Square:
    """
    Este es una clase que define un cuadrado.
    """
    def __init__(self, size=0):
        """
        Inicializa una instancia de Square con un tamaño opcional dado.

        Args:
            size (int, opcional): El tamaño del cuadrado
            (verificación de tipo y valor).
                El valor predeterminado es 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter para obtener el valor del tamaño del cuadrado.

        Returns:
            int: El tamaño del cuadrado.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter para establecer el valor del tamaño
        del cuadrado con verificación.

        Args:
            value (int): El nuevo tamaño del cuadrado.

        Raises:
            TypeError: Si el valor no es un entero.
            ValueError: Si el valor es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calcula y devuelve el área del cuadrado.

        Returns:
            int: El área del cuadrado (lado * lado).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Imprime el cuadrado con caracteres '#' en stdout.
        Si el tamaño es igual a 0, imprime una línea vacía.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
