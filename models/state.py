#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_DEV_STORAGE") == "db":
        @property
        def cities(self):
            """ returns a list of related city objects """
            list_of_cities = []
            for city in list(models.storage.all(City).values()):
                if city.state.id == self.id:
                    list_of_cities.append(city)
            return list_of_cities
