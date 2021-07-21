"""
Constant nodes
"""
from myparser.node.node import Node
import math


def str_to_cons(string_):
    """
    Calculate a pure string's value
    :param string_: pure raw string
    :return: value of string
    """
    if 'pi' in string_:
        if len(string_) != 2:
            return float(string_[:string_.find("pi")]) * math.pi
        else:
            return math.pi
    if 'e' in string_:
        if len(string_) != 1:
            return float(string_[:string_.find("e")]) * math.e
        else:
            return math.e
    return float(string_)


class ConsNode(Node):
    """
    Node represents constants
    """
    def calculate_value(self, x: float):
        """
        Calculate a node's value based on its values.
        :param x is the value of variable x
        :return: value of node
        """
        if 'x' in self.raw_str:
            if len(self.raw_str) == 1:
                self.value = x
            else:
                self.value = str_to_cons(self.raw_str[:self.raw_str.find('x')]) * x
        else:
            self.value = str_to_cons(self.raw_str)
