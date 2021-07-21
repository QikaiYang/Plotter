"""
Abstract class - Node
"""
from abc import ABCMeta, abstractmethod
import string


class Node(metaclass=ABCMeta):
    """
    Abstract node class
    """
    def __init__(self, input_string: string):
        """
        Initialization of a node
        :param input_string the input string to be parsed
        :return: nothing
        """
        self.raw_str = input_string
        self.value = None
        self.children = []

    def assign_child(self, list_child):
        """
        Set a node's children
        :param list_child a list of children to be assigned
        :return: nothing
        """
        self.children = list_child

    @abstractmethod
    def calculate_value(self, x: float):
        """
        Abstract method. Calculate a node's value based on its children's values.
        :param x is the value of variable x
        :return: value of node
        """
        pass
