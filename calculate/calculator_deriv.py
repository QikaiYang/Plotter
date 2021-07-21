"""
Normal calculator class
"""
from calculate.calculator import Calculator
import math


class CalculatorDerivation(Calculator):
    """
    Derivation calculator class
    """

    def get_points(self):
        """
        Get a bunch of points based on function string, lower bound, and higher bound
        :return: 2D list of all points
        """
        x_val = []
        y_val = []
        precision = 100
        for i in range(self.number_points):
            val = self.left + i * (self.right - self.left) / (self.number_points - 1)
            x_val.append(val)
            self.grammar_tree.calculate_value_tree(self.grammar_tree.root, val)
            if str(type(self.grammar_tree.root.value)).find("complex") == -1:
                prev = self.grammar_tree.root.value
            else:
                prev = None
            self.grammar_tree.calculate_value_tree(self.grammar_tree.root, val+precision*(self.right - self.left))
            if str(type(self.grammar_tree.root.value)).find("complex") == -1:
                after = self.grammar_tree.root.value
            else:
                after = None
            if prev is None or after is None:
                y_val.append(None)
            else:
                y_val.append((after-prev)/(precision*(self.right - self.left)))
        return [x_val, y_val]
