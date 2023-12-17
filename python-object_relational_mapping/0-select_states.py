#!/usr/bin/python3
""" Este script enumera todos los 'states'
de la database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

def list_func():
    """Enumera los states de la database"""
    if len(argv) != 4:
        return

    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = database.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    database.close()


if __name__ == "__main__":
    list_func()
