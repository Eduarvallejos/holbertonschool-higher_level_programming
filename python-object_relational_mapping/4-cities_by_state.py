#!/usr/bin/python3
"""
Este script hace que nos conectemos con Mysql.
"""

import MySQLdb
from sys import argv


def list_cities():
    """
    Esta función se conecta al servidor MySQL y enumera todas las ciudades.
    de la base de datos 'hbtn_0e_4_usa'.
    """

    mysql_user = argv[1]
    mysql_pass = argv[2]
    mysql_db = argv[3]
    host_mysql = 'localhost'
    port_mysql = 3306

    database = MySQLdb.connect(
        host=host_mysql,
        port=port_mysql,
        user=mysql_user,
        password=mysql_pass,
        database=mysql_db
    )

    cursor = database.cursor()
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
            """
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
    list_cities()
