#!/usr/bin/python3
""" Database storage module """

from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """ database storage class """
    __engine = None
    __session = None

    def __init__(self):
        """ initializes a new db storage instance """
        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}".format(
                    getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
                pool_pre_ping=True)
        # drop all tables if the environment variable HBNB_ENV is equal to test
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        self.reload()

    def all(self, cls=None):
        """ query on current db session to return all data if cls is not passed
            else return data specific to cls value passed
        """
        if not cls:
            data = self.__session.query(City).all()
            data.extend(self.__session.query(State).all())
            data.extend(self.__session.query(Place).all())
            data.extend(self.__session.query(Review).all())
            data.extend(self.__session.query(Amenity).all())
            data.extend(self.__session.query(User).all())
        else:
            data = self.__session.query(cls).all()
        return {"{}.{}".format(
            type(obj).__name__, obj.id): obj for obj in data}

    def new(self, obj):
        """ adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes obj from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database (feature of SQLAlchemy)
            all classes who inherit from Base must be imported before calling
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """ close the active SQLAlchemy session """
        self.__session.close()
