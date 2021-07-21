"""
Power Node
"""
from myparser.node.node import Node
import string


class PowerNode(Node):
    """
    Node represents power
    """
    def __init__(self, ab_num: float, input_string: string):
        """
        Initialization of a node
        @param input_string the input string to be parsed
        """
        super().__init__(input_string)
        self.raw_str = input_string
        self.value = None
        self.children = []
        self.abbr = ab_num  # store the value of the abbreviation of multiplication

    def calculate_value(self, x: float):
        """
        Calculate a node's value based on its children's values.
        :param x is the value of variable x
        :return: value of node
        """
        if self.children[1].value is None or self.children[0].value is None:
            self.value = None
        else:
            self.value = self.children[0].value ** self.children[1].value
