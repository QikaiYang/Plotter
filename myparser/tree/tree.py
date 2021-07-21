"""
Tree class
"""
from myparser.node.brace_node import BraceNode
from myparser.node.plus_node import PlusNode
from myparser.node.minus_node import MinusNode
from myparser.node.mul_node import MulNode
from myparser.node.div_node import DivNode
from myparser.node.power_node import PowerNode
from myparser.node.constant_node import str_to_cons
from myparser.node.constant_node import ConsNode
from myparser.node.cos_node import CosNode
from myparser.node.sin_node import SinNode
from myparser.node.ln_node import LnNode
from myparser.node.tan_node import TanNode
import string
import re


class GrammarTree:
    """
    A tree represents the grammar of a specific function
    """

    def __init__(self, input_string: string):
        """
        Initialization of a tree
        :param input_string: the input string to be parsed
        """
        self.raw_string = input_string.replace(" ", "")
        self.root = None
        self.transfer_negative_abbr()
        if not self.check_brackets():
            raise Exception("Brackets don't match")

    def check_brackets(self):
        """
        Check if the raw string's brackets are proper
        :return: whether the string's brackets are proper or not
        """
        stack = []
        for i in range(len(self.raw_string)):
            if self.raw_string[i] == '(':
                stack.append('(')
            elif self.raw_string[i] == ')':
                if len(stack) == 0:
                    return False
                elif stack[len(stack) - 1] == ')':
                    return False
                else:
                    stack.pop(len(stack) - 1)
        if len(stack) == 0:
            return True
        return False

    def evaluate_priority(self, input_string):
        """
        Evaluate all the operators' priority of an input string
        :param: an input string
        :return: a list of the priority of all operators in a function
        """
        priority = {"+": 4, "-": 4, "*": 3, "/": 3, "^": 2, "ln": 1, "sin": 1, "cos": 1, "tan": 1}
        # The higher the priority is, the higher the position an operator in the tree should be
        # Brace node has the lowest priority - 0
        op_idx = [(i.start(), i.end()) for i in re.finditer("\+|-|\*|/|\^|\(|\)|ln|tan|cos|sin", input_string)]
        stack = []
        result = []
        for idx in op_idx:
            if input_string[idx[0]:idx[1]] == '(':
                stack.append('(')
                result.append(0)
            elif input_string[idx[0]:idx[1]] == ')':
                stack.pop(len(stack) - 1)
                result.append(0)
            else:
                if len(stack) == 0:
                    result.append(priority[input_string[idx[0]:idx[1]]])
                else:
                    result.append(0)
        return result

    def transfer_negative_abbr(self):
        """
        Check the negative sign of a string and fix it
        :return: nothing
        """
        if self.raw_string[0] == "-":
            self.raw_string = "0" + self.raw_string
        self.raw_string = self.raw_string.replace("+-", "-")
        self.raw_string = self.raw_string.replace("--", "+")
        self.raw_string = self.raw_string.replace("*-", "*(0-1)*")
        self.raw_string = self.raw_string.replace("/-", "/(0-1)/")
        self.raw_string = self.raw_string.replace("(-", "(0-")
        self.raw_string = self.raw_string.replace(")(", ")*(")
        self.raw_string = self.raw_string.replace(")x", ")*x")
        self.raw_string = self.raw_string.replace(")ln", ")*ln")
        self.raw_string = self.raw_string.replace(")tan", ")*tan")
        self.raw_string = self.raw_string.replace(")cos", ")*cos")
        self.raw_string = self.raw_string.replace(")sin", ")*sin")
        for i in (list(range(10)) + ["pi", "e"]):
            self.raw_string = self.raw_string.replace(str(i) + "x", str(i) + "*x")
            self.raw_string = self.raw_string.replace(str(i) + "sin", str(i) + "*sin")
            self.raw_string = self.raw_string.replace(str(i) + "cos", str(i) + "*cos")
            self.raw_string = self.raw_string.replace(str(i) + "tan", str(i) + "*tan")
            self.raw_string = self.raw_string.replace(str(i) + "ln", str(i) + "*ln")
            self.raw_string = self.raw_string.replace(")" + str(i), ")*" + str(i))

    def build_tree(self):
        """
        Build the tree based on the input raw string
        :return: nothing
        """
        self.root = self.help_build_tree(self.raw_string)

    def help_build_tree(self, input_string):
        """
        Helper function of building the tree
        :param input_string: input raw string
        :return: a root of the current subtree
        """
        node_dic = {"+": PlusNode, "-": MinusNode, "*": MulNode, "/": DivNode, "^": PowerNode, "ln": LnNode,
                    "tan": TanNode, "sin": SinNode, "cos": CosNode}
        op_idx = [(i.start(), i.end()) for i in re.finditer("\+|-|\*|/|\^|\(|\)|ln|tan|cos|sin", input_string)]
        curr_priority = self.evaluate_priority(input_string)
        if not curr_priority:  # base case: constant node
            return ConsNode(input_string)
        elif sum(curr_priority) == 0:  # recursive case 1: brace node
            return self.help_build_brace(input_string)
        elif max(curr_priority) == 1:  # recursive case 2: sin/ln/tan/cos
            return self.help_build_unary(curr_priority, input_string, node_dic, op_idx)
        elif max(curr_priority) == 3 or max(curr_priority) == 4:  # recursive case 3: +-*/
            return self.help_build_mul_div_plus_minus(curr_priority, input_string, node_dic, op_idx)
        else:  # recursive case 4: ^
            curr_node = self.help_build_power(curr_priority, input_string, node_dic, op_idx)
            return curr_node

    def help_build_power(self, curr_priority, input_string, node_dic, op_idx):
        """
        helper function of building a power node and its children recursively
        :param curr_priority: a list of priorities
        :param input_string: input raw substring
        :param node_dic: a dictionary of constructors
        :param op_idx: current operator's index
        :return: a subtree with root as a power node
        """
        locate = curr_priority.index(max(curr_priority))
        curr_op = input_string[op_idx[locate][0]:op_idx[locate][1]]
        if input_string[:op_idx[locate][0]].find("(") >= 0:
            if input_string[0] == "(":
                curr_node = node_dic[curr_op](1, input_string)
                child1 = self.help_build_tree(input_string[:op_idx[locate][0]])
                child2 = self.help_build_tree(input_string[op_idx[locate][1]:])
                curr_node.assign_child([child1, child2])
            elif input_string[0] == 's' or input_string[0] == 'l' \
                    or input_string[0] == 't' or input_string[0] == 'c':
                curr_node = node_dic[curr_op](1, input_string)
                child1 = self.help_build_tree(input_string[:op_idx[locate][0]])
                child2 = self.help_build_tree(input_string[op_idx[locate][1]:])
                curr_node.assign_child([child1, child2])
            else:
                curr_node = node_dic[curr_op](str_to_cons(input_string[:input_string.find("(")]), input_string)
                child1 = self.help_build_tree(input_string[input_string.find("("):op_idx[locate][0]])
                child2 = self.help_build_tree(input_string[op_idx[locate][1]:])
                curr_node.assign_child([child1, child2])
        elif input_string[:op_idx[locate][0]].find("x") >= 0:
            if input_string[0] == "x":
                curr_node = node_dic[curr_op](1, input_string)
                child1 = self.help_build_tree(input_string[:op_idx[locate][0]])
                child2 = self.help_build_tree(input_string[op_idx[locate][1]:])
                curr_node.assign_child([child1, child2])
            else:
                curr_node = node_dic[curr_op](str_to_cons(input_string[:input_string.find("x")]), input_string)
                child1 = self.help_build_tree(input_string[input_string.find("x"):op_idx[locate][0]])
                child2 = self.help_build_tree(input_string[op_idx[locate][1]:])
                curr_node.assign_child([child1, child2])
        else:
            curr_node = node_dic[curr_op](1, input_string)
            child1 = self.help_build_tree(input_string[:op_idx[locate][0]])
            child2 = self.help_build_tree(input_string[op_idx[locate][1]:])
            curr_node.assign_child([child1, child2])
        return curr_node

    def help_build_mul_div_plus_minus(self, curr_priority, input_string, node_dic, op_idx):
        """
        helper function of building a plus/minus/mul/div node and its children recursively
        :param curr_priority: a list of priorities
        :param input_string: input raw substring
        :param node_dic: a dictionary of constructors
        :param op_idx: current operator's index
        :return: a subtree with root as a plus/minus/mul/div node
        """
        locate = curr_priority.index(max(curr_priority))
        curr_op = input_string[op_idx[locate][0]:op_idx[locate][1]]
        curr_node = node_dic[curr_op](input_string)
        child1 = self.help_build_tree(input_string[:op_idx[locate][0]])
        child2 = self.help_build_tree(input_string[op_idx[locate][1]:])
        curr_node.assign_child([child1, child2])
        return curr_node

    def help_build_unary(self, curr_priority, input_string, node_dic, op_idx):
        """
        helper function of building a unary node
        :param curr_priority: a list of priorities
        :param input_string: input raw substring
        :param node_dic: a dictionary of constructors
        :param op_idx: current operator's index
        :return: a subtree with root as a unary node
        """
        locate = curr_priority.index(max(curr_priority))
        curr_op = input_string[op_idx[locate][0]:op_idx[locate][1]]
        curr_node = node_dic[curr_op](input_string)
        child = self.help_build_tree(input_string[op_idx[locate][1]:])
        curr_node.assign_child([child])
        return curr_node

    def help_build_brace(self, input_string):
        """
        helper function of building a brace node
        :param input_string: input raw substring
        :return: a subtree with root as a brace node
        """
        if input_string[0] == "(":
            curr_node = BraceNode(1, input_string)
            child = self.help_build_tree(input_string[1:len(input_string) - 1])
            curr_node.assign_child([child])
            return curr_node
        else:
            curr_node = BraceNode(float(input_string[:input_string.find("(")]), input_string)
            child = self.help_build_tree(input_string[input_string.find("(") + 1:len(input_string) - 1])
            curr_node.assign_child([child])
            return curr_node

    def postorder_traversal(self, node, input_list):
        """
        postorder traversal of the tree, return a list
        :param: the start node
        :param: input empty list
        :return: a list of objects in the tree with post order
        """
        if not node.children:
            input_list.append((str(node), node.raw_str))
        else:
            for child in node.children:
                self.postorder_traversal(child, input_list)
            input_list.append((str(node), node.raw_str))

    def calculate_value_tree(self, node, value):
        """
        Calculate the value of y given x
        :param node: current node
        :param value: x value
        :return: y value
        """
        if not node.children:
            node.calculate_value(value)
        else:
            for child in node.children:
                self.calculate_value_tree(child, value)
            node.calculate_value(value)
