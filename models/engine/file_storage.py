#!/usr/bin/python3
"""that serializes instances to a JSON file and deserializes JSON file"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """class FileStorage"""

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ add an object in the dictionary "__objects" using 
        the class name and its attribute id """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        _dict = {"BaseModel": BaseModel}
        try:
            with open(self.__file_path, 'r') as file:
                for key, value in json.load(file).items():
                    cls = value["__class__"]
                    clas = _dict[cls]
                    obj = clas(**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
