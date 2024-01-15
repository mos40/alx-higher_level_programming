#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Base model.

    Represents the "base" for all other classes in project XYZ.

    Private Class Attributes:
        __obj_counter (int): Number of instantiated Base objects.
    """

    __obj_counter = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The id of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__obj_counter += 1
            self.id = Base.__obj_counter

    @staticmethod
    def to_json_string(list_of_dicts):
        """Return the JSON serialization of a list of dictionaries.

        Args:
            list_of_dicts (list): A list of dictionaries.
        """
        if not list_of_dicts:
            return "[]"
        return json.dumps(list_of_dicts)

    @classmethod
    def save_to_file(cls, object_list):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            object_list (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if not object_list:
                jsonfile.write("[]")
            else:
                list_of_dicts = [obj.to_dictionary() for obj in object_list]
                jsonfile.write(Base.to_json_string(list_of_dicts))

    @staticmethod
    def from_json_string(json_str):
        """Return the deserialization of a JSON string.

        Args:
            json_str (str): A JSON str representation of a list of dicts.
        Returns:
            If json_str is None or empty - an empty list.
            Otherwise - the Python list represented by json_str.
        """
        if not json_str or json_str == "[]":
            return []
        return json.loads(json_str)

    @classmethod
    def create(cls, **attrs):
        """Return a class instantiated from a dictionary of attributes.

        Args:
            **attrs (dict): Key/value pairs of attributes to initialize.
        """
        if attrs and attrs != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**attrs)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_of_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_of_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, object_list):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            object_list (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if not object_list or object_list == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in object_list:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(rectangle_list, square_list):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            rectangle_list (list): A list of Rectangle objects to draw.
            square_list (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in rectangle_list:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in square_list:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for _ in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
