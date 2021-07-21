"""
Calculator Abstract Class
"""
from abc import ABCMeta, abstractmethod
from myparser.tree.tree import GrammarTree
import string


class Calculator(metaclass=ABCMeta):
    """
    Abstract class of calculator
    """

    def __init__(self, input_string: string, low_bound: float, high_bound: float, number: int):
        """
        Constructor of the abstract calculator
        :param input_string: input raw string
        :param low_bound: lower bound
        :param high_bound: higher bound
        :param number: number of points that need to be plotted
        """
        self.raw_string = input_string
        self.left = low_bound
        self.right = high_bound
        self.number_points = number
        self.grammar_tree = GrammarTree(self.raw_string)
        self.grammar_tree.build_tree()

    @abstractmethod
    def get_points(self):
        """
        Abstract method. Calculate a 2D array of points for this calculator class based on the input function
        :return: a 2D array of all points need to be plotted
        """
        pass
