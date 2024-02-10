#!/usr/bin/python3
"""Base model script"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base model for all classes"""

    def __init__(self, *args, **kwargs):
        """Constructor method"""

        for key, value in kwargs.items():
            if key == "__class__":
                continue
            if key == "created_at" or key == "updated_at":
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            setattr(self, key, value)
        if "id" not in kwargs.keys():
            self.id = str(uuid.uuid4())
        if "created_at" not in kwargs.keys():
            self.created_at = datetime.now()
        if "updated_at" not in kwargs.keys():
            self.updated_at = datetime.now()
        if len(kwargs) == 0:
            storage.new(self)

    def __str__(self):
        """to print in str format"""
        return "[{:s}] ({:s}) {:s}".format(
            self.__class__.__name__, self.id, str(self.__dict__)
        )

    def save(self):
        """to update the creation time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """to print in dictionary format"""
        _copy = self.__dict__.copy()
        _copy["__class__"] = self.__class__.__name__
        _copy["created_at"] = self.created_at.isoformat()
        _copy["updated_at"] = self.updated_at.isoformat()
        return _copy
