#!/usr/bin/python3
"""
Define una clase Mylist que hereda de la clase list.
"""


class MyList(list):
    """
    Metodo de instansia que imprime la lista ordenada de forma ascendente.
    """
    def print_sorted(self):
        """
        Ordena la lista actual y la almacena en sorted_list
        """
        sorted_list = sorted(self)
        print(sorted_list)
