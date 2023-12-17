#!/usr/bin/python3
""" Este script enumera todos los 'states'
de la database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv


def list():
    """
    Esta función hace una consulta a  
    la db hbtn_0e_0_usa.
    """

    database = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        port=3306,
        database=argv[3]
    )
    cur = database.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    database.close()


if __name__ == "__main__":
    """
    Esta validación evita que se ejecute
    este archivo.
    """
    list()
