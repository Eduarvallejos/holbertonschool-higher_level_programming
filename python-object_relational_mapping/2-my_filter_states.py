#!/usr/bin/python3
"""
Este script hace que nos conectemos con Mysql.
"""

import MySQLdb
from sys import argv


def search_state_by_name():
    """
    Esta función se conecta al servidor MySQL recupera y muestra
    todos los valores en la tabla de estados donde el nombre coincide
    con el argumento proporcionado.
    """

    mysql_user = argv[1]
    mysql_pass = argv[2]
    mysql_db = argv[3]
    host_mysql = 'localhost'
    port_mysql = 3306
    state_name = argv[4]

    database = MySQLdb.connect(
        host=host_mysql,
        port=port_mysql,
        user=mysql_user,
        password=mysql_pass,
        database=mysql_db
    )

    cursor = database.cursor()
    query = "SELECT * FROM states WHERE BINARY\
            name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    database.close()


if __name__ == "__main__":
    """
    Esta validación evita que se ejecute
    este archivo.
    """
    search_state_by_name()
