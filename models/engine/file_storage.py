#!/usr/bin/python3
"""the file storage"""


import json


class FileStorage:
    """file storgae"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return file dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """to save new obj with its class name"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """to save to json files"""
        jsn_dic = {}
        for key, value in FileStorage.__objects.items():
            jsn_dic[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF8") as f:
            json.dump(jsn_dic, f)

    def reload(self):
        """to return the value of json string int python obj"""
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as f:
                from models.base_model import BaseModel
                from models.user import User
                p_obj = json.load(f)
                for key, value in p_obj.items():
                    objClassName = value["__class__"]
                    objClassValue = eval(objClassName + "(**value)")
                    self.new(objClassValue)
        except IOError:
            pass
