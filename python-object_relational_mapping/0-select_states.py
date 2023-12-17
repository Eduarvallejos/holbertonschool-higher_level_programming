#!/usr/bin/python3
""" Este script enumera todos los 'states' de la database hbtn_0e_0_usa."""

import MySQLdb
from sys import argv

def states():
    if len(argv) != 4:
        return

    database = MySQLdb.connect(
            host="localhost",
            port="3306",
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.ferchall()
    for row in rows:
        print(row)

    cursor.close()
    database.close()

if __name__ == "__main__":
    states()
