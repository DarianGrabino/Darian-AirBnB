#!/usr/bin/python3
"""BaseModel class"""
import uuid
from datetime import datetime
import models

format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """Define class"""

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, format)
                if key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id =str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """define la representación en forma de cadena de un objeto"""
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        result_dict = self.__dict__.copy()
        result_dict["__class__"] = self.__class__.__name__
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        return result_dict
