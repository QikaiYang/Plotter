from myparser.tree.tree import GrammarTree
import unittest
import math


class TestTree(unittest.TestCase):
    def help_check(self, list1, list2):
        """
        helper function check if two lists of items are equal
        :param list1: the estimated list
        :param list2: the reference list
        :return: nothing
        """
        for i in range(len(list2)):
            self.assertEqual(list1[i][0].find(list2[i][0]) >= 0, True)
            self.assertEqual(list1[i][1], list2[i][1])

    def test_simple(self):
        """
        test if the tree is constructed correctly given some simple expression
        :return: nothing
        """
        tree1 = GrammarTree("x")
        tree1.build_tree()
        tree1_check = [("ConsNode", "x")]
        tree_list1 = []
        tree1.postorder_traversal(tree1.root, tree_list1)

        tree2 = GrammarTree("2*x")
        tree2.build_tree()
        tree2_check = [("ConsNode", "2"), ("ConsNode", "x"), ("MulNode", "2*x")]
        tree_list2 = []
        tree2.postorder_traversal(tree2.root, tree_list2)

        tree3 = GrammarTree("sin(x)")
        tree3.build_tree()
        tree3_check = [("ConsNode", "x"), ("BraceNode", "(x)"), ("SinNode", "sin(x)")]
        tree_list3 = []
        tree3.postorder_traversal(tree3.root, tree_list3)

        tree4 = GrammarTree("cos(x)")
        tree4.build_tree()
        tree4_check = [("ConsNode", "x"), ("BraceNode", "(x)"), ("CosNode", "cos(x)")]
        tree_list4 = []
        tree4.postorder_traversal(tree4.root, tree_list4)

        self.help_check(tree_list1, tree1_check)
        self.help_check(tree_list2, tree2_check)
        self.help_check(tree_list3, tree3_check)
        self.help_check(tree_list4, tree4_check)

    def test_medium(self):
        """
        test if the tree is constructed correctly given some medium-hard cases
        :return: nothing
        """
        tree1 = GrammarTree("x+3.3pi")
        tree1.build_tree()
        tree_list1 = []
        tree1.postorder_traversal(tree1.root, tree_list1)
        tree1_check = [("ConsNode", "x"), ("ConsNode", "3.3pi"), ("PlusNode", "x+3.3pi")]

        tree2 = GrammarTree("-ex + 5")
        tree2.build_tree()
        tree_list2 = []
        tree2.postorder_traversal(tree2.root, tree_list2)
        tree2_check = [("ConsNode", "0"), ("ConsNode", "e"), ("ConsNode", "x"), ("MulNode", "e*x"), ("ConsNode", "5"),
                       ("PlusNode", "e*x+5"), ("MinusNode", "0-e*x+5")]

        tree3 = GrammarTree("-2.0(-x^pi)")
        tree3.build_tree()
        tree_list3 = []
        tree3.postorder_traversal(tree3.root, tree_list3)
        tree3_check = [("ConsNode", "0"), ("ConsNode", "0"), ("ConsNode", "x"), ("ConsNode", "pi"),
                       ("PowerNode", "x^pi"), ("MinusNode", "0-x^pi"), ("BraceNode", "2.0(0-x^pi)"),
                       ("MinusNode", "0-2.0(0-x^pi)")]

        self.help_check(tree_list1, tree1_check)
        self.help_check(tree_list2, tree2_check)
        self.help_check(tree_list3, tree3_check)

    def test_complex(self):
        """
        test if the tree is constructed correctly given a complex expression
        :return:
        """
        tree1 = GrammarTree("sin(ln(cos(1+x^2*x)))")
        tree1.build_tree()
        tree_list1 = []
        tree1.postorder_traversal(tree1.root, tree_list1)
        tree1_check = [('ConsNode', '1'), ('ConsNode', 'x'), ('ConsNode', '2'), ('PowerNode', 'x^2'),
                       ('ConsNode', 'x'), ('MulNode', 'x^2*x'), ('PlusNode', '1+x^2*x'), ('BraceNode', '(1+x^2*x)'),
                       ('CosNode', 'cos(1+x^2*x)'), ('BraceNode', '(cos(1+x^2*x))'), ('LnNode', 'ln(cos(1+x^2*x))'),
                       ('BraceNode', '(ln(cos(1+x^2*x)))'), ('SinNode', 'sin(ln(cos(1+x^2*x)))')]
        self.help_check(tree_list1, tree1_check)

    def test_simple_bracket(self):
        """
        special test case for simple brackets
        :return: nothing
        """
        tree1 = GrammarTree("2(x+1)^2 + pix^0.5")
        tree1.build_tree()
        tree_list1 = []
        tree1.postorder_traversal(tree1.root, tree_list1)
        tree1_check = [('ConsNode', 'x'), ('ConsNode', '1'), ('PlusNode', 'x+1'),
                       ('BraceNode', '(x+1)'), ('ConsNode', '2'), ('PowerNode', '2(x+1)^2'),
                       ('ConsNode', 'pi'), ('ConsNode', 'x'), ('ConsNode', '0.5'),
                       ('PowerNode', 'x^0.5'), ('MulNode', 'pi*x^0.5'), ('PlusNode', '2(x+1)^2+pi*x^0.5')]
        self.help_check(tree_list1, tree1_check)

    def test_multiple_brackets(self):
        """
        special test case for multiple test cases
        :return:
        """
        tree1 = GrammarTree("((2x^2)+(2/x+pi))(pi+e)")
        tree1.build_tree()
        tree_list1 = []
        tree1.postorder_traversal(tree1.root, tree_list1)
        tree1_check = [('ConsNode', '2'), ('ConsNode', 'x'), ('ConsNode', '2'), ('PowerNode', 'x^2'),
                       ('MulNode', '2*x^2'), ('BraceNode', '(2*x^2)'), ('ConsNode', '2'),
                       ('ConsNode', 'x'), ('DivNode', '2/x'), ('ConsNode', 'pi'), ('PlusNode', '2/x+pi'),
                       ('BraceNode', '(2/x+pi)'), ('PlusNode', '(2*x^2)+(2/x+pi)'),
                       ('BraceNode', '((2*x^2)+(2/x+pi))'), ('ConsNode', 'pi'), ('ConsNode', 'e'), ('PlusNode', 'pi+e'),
                       ('BraceNode', '(pi+e)'), ('MulNode', '((2*x^2)+(2/x+pi))*(pi+e)')]
        self.help_check(tree_list1, tree1_check)

    def test_cal_simple(self):
        """
        test if the y value can be calculated corrected given some simple expression
        :return:
        """
        tree1 = GrammarTree("2(x^0.5+1)")
        tree1.build_tree()
        tree1.calculate_value_tree(tree1.root, 3)

        tree2 = GrammarTree("sin(x)")
        tree2.build_tree()
        tree2.calculate_value_tree(tree2.root, 3)

        tree3 = GrammarTree("2(x-1)(x+1)")
        tree3.build_tree()
        tree3.calculate_value_tree(tree3.root, 3)

        tree4 = GrammarTree("2cos(x-1)sin(x+1)")
        tree4.build_tree()
        tree4.calculate_value_tree(tree4.root, 3)

    def test_cal_medium(self):
        """
        test if the y value can be calculated corrected given some medium-hard expression
        :return: nothing
        """
        tree1 = GrammarTree("(x-0.7*2)(3.1/x)(x^5+3)")
        tree1.build_tree()
        tree1.calculate_value_tree(tree1.root, 3)

        tree2 = GrammarTree("cos(tan(ln(sin(x^2-2*x))))")
        tree2.build_tree()
        tree2.calculate_value_tree(tree2.root, 3)

        tree3 = GrammarTree("2((x-1.1)(x^1.5))(5^x)")
        tree3.build_tree()
        tree3.calculate_value_tree(tree3.root, 3)

        tree4 = GrammarTree("2(cos(x-1)sin(x+1))*(pi+e)")
        tree4.build_tree()
        tree4.calculate_value_tree(tree4.root, 3)

        self.assertEqual(tree1.root.value, (3 - 0.7 * 2) * (3.1 / 3) * (3 ** 5 + 3))
        self.assertEqual(tree2.root.value, math.cos(math.tan(math.log(math.sin(3 ** 2 - 2 * 3)))))
        self.assertEqual(tree3.root.value, 2 * ((3 - 1.1) * (3 ** 1.5)) * (5 ** 3))
        self.assertEqual(tree4.root.value, 2 * (math.cos(3 - 1) * math.sin(3 + 1)) * (math.pi + math.e))

    def test_cal_complex(self):
        """
        test if the y value can be calculated corrected given some complex expression
        :return: nothing
        """
        tree1 = GrammarTree("2sin(x)x^3/x")
        tree1.build_tree()
        tree1.calculate_value_tree(tree1.root, 3)

        tree2 = GrammarTree("cos(sin(cos(sin((x-1.0*2)(3/x)(x^2-3)))))")
        tree2.build_tree()
        tree2.calculate_value_tree(tree2.root, 3)

        tree3 = GrammarTree("2(x+3)(tan(2))^(sin(x)^x)")
        tree3.build_tree()
        tree3.calculate_value_tree(tree3.root, 2)

        self.assertEqual(round(tree1.root.value, 3), round((2 * math.sin(3) * 3 ** 3 / 3), 3))
        self.assertEqual(round(tree2.root.value, 3),
                         round(math.cos(math.sin(math.cos(math.sin((3 - 1.0 * 2) * (3 / 3) * (3 ** 2 - 3))))), 3))
        self.assertEqual(tree3.root.value, 2 * (2 + 3) * (math.tan(2)) ** (math.sin(2) ** 2))

    def test_error(self):
        """
        test if the tree's constructor can catch some invalid inputs
        :return:
        """
        try:
            tree1 = GrammarTree("())")
            self.assertEqual(1, 0)
        except:
            self.assertEqual(1, 1)
        try:
            tree1 = GrammarTree("(()")
            self.assertEqual(1, 0)
        except:
            self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
