#!/usr/bin/python3

"""Define a class Square."""


class Node:
    """Represent a square."""

    def __init__(self, data, position=None):
        """Initialize a new square.

        Args:
            data (int): The data of the new square.
            position (int, int): The position of the new square.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the current data data of the square."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def position(self):
        """Get/set the position of the Node."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("position must be a Node object")
        self.__position = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.position = None
            self.__head = new
        elif self.__head.data > value:
            new.position = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.position is not None and
                    tmp.position.data < value):
                tmp = tmp.position
            new.position = tmp.position
            tmp.position = new

    def __str__(self):
        """Define the print() representation of a Square."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.position
        return ('\n'.join(values))
