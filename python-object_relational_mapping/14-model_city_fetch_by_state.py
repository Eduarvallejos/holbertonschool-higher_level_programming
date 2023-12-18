#!/usr/bin/python3
"""
Este script imprime todos los objetos de la ciudad
de la base de datos 'hbtn_0e_14_usa'
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state():
    """
    Se conecta al servidor MySQL e imprime todos los objetos de la ciudad
    de un estado específico.
    """

    user = arv[1]
    password = argv[2]
    db = argv[3]
    host = 'localhost'
    port = 3306

    engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}:{port}/{db}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    fetch_cities_by_state()
