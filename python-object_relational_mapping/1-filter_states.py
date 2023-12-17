#!/usr/bin/python3
"""
Esta función recupera e imprime los states con nombres
que comienzan con 'N' de la base de datos hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

def list_states_with_N():
    """
    Ejecute la consulta para recuperar states que
    comiencen con 'N' y ordenados por states.id.
    """
    database = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        port=3306,
        database=argv[3],
        )

    cursor = database.cursor()
    cursor.execute("""SELECT * FROM states
                    WHERE name
                    LIKE 'N%'
                    ORDER BY id ASC
                    """)
    rows = cursor.fetchall()

    for row in rows:
        print(row)


    cursor.close()
    database.close()

if __name__ == "__main__":
    list_states_with_N()
