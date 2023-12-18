#!/usr/bin/python3
"""
Este módulo define la clase Ciudad.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

class City(Base):
    """
    Clase de ciudad vinculada a la tabla MySQL 'ciudades
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    
    state = relationship("State", back_populates="cities")
