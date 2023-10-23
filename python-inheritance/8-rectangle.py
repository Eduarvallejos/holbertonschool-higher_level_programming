#!/usr/bin/python3
"""
definimos una clase Rectangle que herda de BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    La clase rectangle hereda a Basegeometry.
    """
    def __init__(self, width, height):
        """
        Inicializa los atributos privados de ancho y alto.
        """
        self.__width = width
        self.__height = height
        """
        Llama al método integer_validator de la clase base para validar
        si el ancho y el alto son enteros.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
