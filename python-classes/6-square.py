#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
        Inicializa una instancia de Square con un tamaño opcional
        y una posición opcional.

        Args:
            size (int, opcional): El tamaño del cuadrado
            (verificación de tipo y valor).
                El valor predeterminado es 0.
            position (tuple, opcional): La posición del cuadrado como
            una tupla de 2 enteros.
                El valor predeterminado es (0, 0).
        """
        self.size = size
        self.position = position

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
        Setter para establecer el valor del tamaño del
        cuadrado con verificación.

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

    @property
    def position(self):
        """
        Getter para obtener el valor de la posición del cuadrado.

        Returns:
            tuple: La posición del cuadrado como una tupla de 2 enteros.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter para establecer el valor de la posición del
        cuadrado con verificación.

        Args:
            value (tuple): La nueva posición del cuadrado como una
            tupla de 2 enteros.

        Raises:
            TypeError: Si value no es una tupla de 2 enteros positivos.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                any(map(lambda x: not isinstance(x, int) or x < 0, value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__position = value

    def area(self):
        """
        Calcula y devuelve el área del cuadrado.

        Returns:
            int: El área del cuadrado (lado * lado).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Imprime el cuadrado con caracteres '#' en stdout y
        con una posición especificada.

        Si la posición vertical (position[1]) es mayor que 0;
        no llena las líneas con espacios.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
