#!/usr/bin/python3
"""Base module"""


import json
import csv


class Base:
    """Base class that manage id attribute in all future
    classes and to avoid duplicating the same code.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method to initialize Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries is []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        new_file = "{}.json".format(cls.__name__)
        list_dic = []

        if list_objs is not None:
            for element in list_objs:
                list_dic.append(cls.to_dictionary(element))
        with open(new_file, mode="w", encoding='utf-8') as my_file:
            my_file.write(cls.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Square":
            dummy = cls(2)
            dummy.update(**dictionary)
            return dummy

        if cls.__name__ == "Rectangle":
            dummy = cls(2, 4)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, mode="r", encoding='utf-8') as myfile:
                text = Base.from_json_string(myfile.readline())
                ins_list = []
                for element in text:
                    ins_list.append(cls.create(**element))
                return ins_list
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method that serializes in CSV"""

        csv_file = "{}.csv".format(cls.__name__)
        with open(csv_file, mode='w', newline='') as csv_f:
            if list_objs is None or list_objs is []:
                csv_f.write("[]")
            else:
                if cls.__name__ is 'Rectangle':
                    fields = ["id", "width", "height", "x", "y"]
                if cls.__name__ is 'Square':
                    fields = ["id", "size", "x", "y"]
                doc = csv.DictWriter(csv_f, fieldnames=fields)
                [doc.writerow(obj.to_dictionary()) for obj in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        """ Method that deserializes in CSV"""
        csv_file = '{}.csv'.format(cls.__name__)
        try:
            with open(csv_file, mode='r', newline='') as csv_f:
                if cls.__name__ is 'Square':
                    fields = ["id", "size", "x", "y"]
                else:
                    fields = ["id", "width", "height", "x", "y"]
                dicts_list = csv.DictReader(csv_f, fieldnames=fields)
                dicts_list = [{key: int(value) for key, value in dic.items()}
                              for dic in dicts_list]
                return [cls.create(**dicts) for dicts in dicts_list]
        except IOError:
            return []
