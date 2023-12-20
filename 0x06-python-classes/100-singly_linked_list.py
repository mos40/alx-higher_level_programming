#!/usr/bin/python3

"""Define a class Square."""


class Node:
    """Represent a square."""

    def __init__(self, size, position=None):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self._size = size
        self._position = position

    @property
    def size(self):
        """Get/set the current size size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

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
        elif self.__head.size > value:
            new.position = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.position is not None and
                    tmp.position.size < value):
                tmp = tmp.position
            new.position = tmp.position
            tmp.position = new

    def __str__(self):
        """Define the print() representation of a Square."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.size))
            tmp = tmp.position
        return ('\n'.join(values))
