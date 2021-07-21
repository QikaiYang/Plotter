"""
Tan Node
"""
from myparser.node.node import Node
import math


class TanNode(Node):
    """
    Node represents tan
    """
    def calculate_value(self, x: float):
        """
        Calculate a node's value based on its values.
        :param x is the value of variable x
        :return: value of node
        """
        if self.children[0].value is None:
            self.value = None
        else:
            self.value = math.tan(self.children[0].value)
