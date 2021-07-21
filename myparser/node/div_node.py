"""
Division Node
"""
from myparser.node.node import Node


class DivNode(Node):
    """
    Node represents division
    """
    def calculate_value(self, x: float):
        """
        Calculate a node's value based on its children's values.
        :param x is the value of variable x
        :return: value of node
        """
        if self.children[1].value == 0 or self.children[1].value is None or self.children[0].value is None:
            self.value = None
        else:
            self.value = self.children[0].value / self.children[1].value
