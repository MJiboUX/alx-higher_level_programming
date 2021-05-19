#!/usr/bin/python3
"""Node  class definintion """


class Node:
    """ Node  class defined
        Attributes:
            size (int): data of node
    """
    def __init__(self, data, next_node=None):
        """initializes
        Args:
            data (int): data
            next_node: next_node
        Returns:
            None
        """
        self.data = data
        self.next_node = None

    @property
    def data(self):
        """
        getter of data
        Return:
            data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter of data
        Args:
            value (int): data
        Raises
            TypeError: if data is not int
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    
    @property
    def next_node(self):
        """
        getter of node
        Return:
            node
        """
        return self.__next_node

      
    @next_node.setter
    def next_node(self, value):
        """
        Setter of next_node
        Args:
            value (int): next_node
        Raises
            TypeError: if data is not int
        Returns:
            None
        """
        if not isinstance(value, Node) and value != None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value
