"""
Normal calculator class
"""
from calculate.calculator import Calculator
import math


class CalculatorNormal(Calculator):
    """
    Normal calculator class
    """

    def get_points(self):
        """
        Get a bunch of points based on function string, lower bound, and higher bound
        :return: 2D list of all points
        """
        x_val = []
        y_val = []
        for i in range(self.number_points):
            val = self.left + i * (self.right - self.left) / (self.number_points - 1)
            x_val.append(val)
            self.grammar_tree.calculate_value_tree(self.grammar_tree.root, val)
            if str(type(self.grammar_tree.root.value)).find("complex") == -1:
                y_val.append(self.grammar_tree.root.value)
            else:
                y_val.append(None)
        return [x_val, y_val]

