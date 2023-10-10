#!/usr/bin/python3
"""
Esta modulo representa una clase Rectangle.
"""

class Rectangle:
    """
    Este es una clase que define un rectangulo.
    """
    def __init__(self, width=0,hight=0):

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width
