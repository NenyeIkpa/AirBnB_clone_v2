#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String

if models.storage_type == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    if models.storage_type == "db":
        id = Column(String(60), primary_key=True, nullable=False, unique=True)
        created_at = Column(
                DateTime(),
                default=datetime.utcnow(),
                nullable=False
                )
        updated_at = Column(
                DateTime(),
                default=datetime.utcnow(),
                nullable=False
                )

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        if kwargs:
            # date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                else:
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        dt = self.__dict__.copy()
        dt.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, dt)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        obj_dict = self.__dict__.copy()
        if "created_at" in obj_dict:
            obj_dict['created_at'] = self.created_at.isoformat()
        if "updated_at" in obj_dict:
            obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict.pop('sa_instance_state', None)
        return obj_dict

    def delete(self):
        """ deletes the current instance from the storage """
        models.storage.delete(self)
