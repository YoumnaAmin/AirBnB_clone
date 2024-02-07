#!/usr/bin/python3
"""Base model script"""


import json
import uuid
from datetime import datetime

class BaseModel:
    """Base model for all classes"""

    def __init__(self):
        #for key, value in kwargs.items():
           # if key == "created_at" or key == "updated_at":
               # value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
           # setattr(self, key, value)
        #if "id" not in kwargs.keys():
            self.id = str(uuid.uuid4())
       # if "created_at" not in kwargs.keys():
            self.created_at = datetime.now()
        #if "updated_at" not in kwargs.keys():
            self.updated_at = datetime.now()

    def __str__(self):
        return "[{:s}] ({:s}) {:s}".format(
            self.__class__.__name__, self.id, str(self.__dict__)
        )
    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        _copy = self.__dict__.copy()
        _copy["__class__"] = self.__class__.__name__
        _copy["created_at"] = self.created_at.isoformat()
        _copy["updated_at"] = self.updated_at.isoformat()
        return _copy
