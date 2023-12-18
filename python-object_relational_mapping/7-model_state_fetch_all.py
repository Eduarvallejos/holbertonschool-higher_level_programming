#!/usr/bin/python3
"""
Este script enumera todos los objetos de estado
de la base de datos 'hbtn_0e_6_usa'
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states():
    """
    Se conecta al servidor MySQL y enumera todos los objetos de estado.
    """
    user, password, db = argv[1:4]
    host = 'localhost'
    port = 3306

    engine = create_engine(
        f"mysql://{user}:{password}@{host}:{port}/{db}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()

if __name__ == "__main__":
    list_states()
