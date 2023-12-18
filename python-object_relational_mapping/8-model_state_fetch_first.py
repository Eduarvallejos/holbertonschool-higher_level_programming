#!/usr/bin/python3
"""
Este módulo se conecta a MySql a través sqlalchmemy(ORM).
Este script imprime el primer objeto Estado de la base de datos 'hbtn_0e_6_usa'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_first_state():
    """
    Se conecta al servidor MySQL e imprime el primer objeto de estado.
    """

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@{host}:{port}/{db_name}',
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()

    if state:
        print(f'{state.id}: {state.name}')
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    print_first_state()
