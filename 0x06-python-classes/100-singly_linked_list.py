#!/usr/bin/python3
"""Node Class

    Raises:
        TypeError: for data type mismatch
        TypeError: for next_node type mismatch

    Returns:
        object: node object
    """


class Node:
    """Node Class
    """

    def __init__(self, data, next_node=None):
        """instantiate

        Args:
            data (int): data objet
            next_node (Node, optional): next node pointer. Defaults to None.
        """
        self.data = data
        self.next_node: Node = next_node

    @property
    def data(self):
        """data getter

        Returns:
            int: data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """data setter

        Args:
            value (int): new data

        Raises:
            TypeError: data must be an int
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node getter

        Returns:
            Node: new node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter

        Args:
            value (Node): next node

        Raises:
            TypeError: nexT_node must be a node object
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""SinglyLinkedList class

    Returns:
        SinglyLinkedList: single linked list
"""


class SinglyLinkedList:
    """Singly linked list
    """

    def __init__(self):
        """ Instantiation of linked list"""
        self.__head: Node = None

    def __str__(self) -> str:
        """Printable structure of the class"""
        values = []
        tmp = self.__head
        while tmp:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(values))

    def sorted_insert(self, value):
        """inserts at a sorted position

        Args:
            value (int): value to be inserted
        """
        new = Node(value)

        if not self.__head:
            new.next_node = None
            self.__head = new
            return

        if self.__head.data > new.data:
            new.next_node = self.__head
            self.__head = new
            return

        curr = self.__head
        while (curr.next_node and curr.next_node.data < new.data):
            curr = curr.next_node

        new.next_node = curr.next_node
        curr.next_node = new
