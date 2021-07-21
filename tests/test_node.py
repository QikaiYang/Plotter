from myparser.node.brace_node import BraceNode
from myparser.node.plus_node import PlusNode
from myparser.node.minus_node import MinusNode
from myparser.node.mul_node import MulNode
from myparser.node.div_node import DivNode
from myparser.node.power_node import PowerNode
from myparser.node.constant_node import ConsNode
from myparser.node.cos_node import CosNode
from myparser.node.sin_node import SinNode
from myparser.node.ln_node import LnNode
from myparser.node.tan_node import TanNode
import unittest
import math


def generate_cons():
    con1 = ConsNode("23.4")
    con1.calculate_value(1.1)
    con2 = ConsNode("2x")
    con2.calculate_value(1.1)
    con3 = ConsNode("pi")
    con3.calculate_value(1.1)
    con4 = ConsNode("2.0pi")
    con4.calculate_value(1.1)
    return con1, con2, con3, con4


class TestNode(unittest.TestCase):
    def test_constant(self):
        """
        Test constant node
        :return: nothing
        """
        con1, con2, con3, con4 = generate_cons()
        self.assertEqual(con1.value, 23.4)
        self.assertEqual(con2.value, 2.2)
        self.assertEqual(round(con3.value, 3), round(math.pi, 3))
        self.assertEqual(round(con4.value, 3), round(2 * math.pi, 3))

    def test_plus(self):
        """
        Test plus node
        :return: nothing
        """
        con1, con2, con3, con4 = generate_cons()
        plus1 = PlusNode("random string")
        plus2 = PlusNode("random string")
        plus1.assign_child([con1, con2])
        plus1.calculate_value(1.1)
        plus2.assign_child([con3, con4])
        plus2.calculate_value(1.1)
        self.assertEqual(plus1.value, 23.4 + 2 * 1.1)
        self.assertEqual(round(plus2.value, 3), round(3 * math.pi, 3))

    def test_minus(self):
        """
        Test minus node
        :return: nothing
        """
        con1, con2, con3, con4 = generate_cons()
        minus1 = MinusNode("random string")
        minus2 = MinusNode("random string")
        minus1.assign_child([con1, con2])
        minus1.calculate_value(1.1)
        minus2.assign_child([con3, con4])
        minus2.calculate_value(1.1)
        self.assertEqual(minus1.value, 23.4 - 2 * 1.1)
        self.assertEqual(round(minus2.value, 3), round(math.pi - 2 * math.pi, 3))

    def test_mul(self):
        """
        Test multiplication node
        :return: nothing
        """
        con1, con2, con3, con4 = generate_cons()
        mul1 = MulNode("random string")
        mul2 = MulNode("random string")
        mul1.assign_child([con1, con2])
        mul1.calculate_value(1.1)
        mul2.assign_child([con3, con4])
        mul2.calculate_value(1.1)
        self.assertEqual(mul1.value, 23.4 * 2 * 1.1)
        self.assertEqual(round(mul2.value, 3), round(math.pi * (2 * math.pi), 3))

    def test_div(self):
        """
        Test division node
        :return: nothing
        """
        con1, con2, con3, con4 = generate_cons()
        div1 = DivNode("random string")
        div2 = DivNode("random string")
        div1.assign_child([con1, con2])
        div1.calculate_value(1.1)
        div2.assign_child([con3, con4])
        div2.calculate_value(1.1)
        self.assertEqual(div1.value, 23.4 / (2 * 1.1))
        self.assertEqual(round(div2.value, 3), round(math.pi / (2 * math.pi), 3))

    def test_power(self):
        """
        Test division node
        :return: nothing
        """
        con1, con2, con3, con4 = generate_cons()
        pow1 = PowerNode(1, "random string")
        pow2 = PowerNode(1, "random string")
        pow1.assign_child([con1, con2])
        pow1.calculate_value(1.1)
        pow2.assign_child([con3, con4])
        pow2.calculate_value(1.1)
        self.assertEqual(pow1.value, 23.4 ** (2 * 1.1))
        self.assertEqual(round(pow2.value, 3), round(math.pi ** (2 * math.pi), 3))

    def test_sin(self):
        """
        Test sin node
        :return: nothing
        """
        con1, con2, con3, con4 = generate_cons()
        sin1 = SinNode("random string")
        sin2 = SinNode("random string")
        sin3 = SinNode("random string")
        sin1.assign_child([con1])
        sin1.calculate_value(1.1)
        sin2.assign_child([con2])
        sin2.calculate_value(1.1)
        sin3.assign_child([con4])
        sin3.calculate_value(1.1)
        self.assertEqual(sin1.value, math.sin(23.4))
        self.assertEqual(sin2.value, math.sin(2 * 1.1))
        self.assertEqual(sin3.value, math.sin(2.0 * math.pi))

    def test_cos(self):
        """
        Test cos node
        :return: nothing
        """
        con1, con2, con3, con4 = generate_cons()
        cos1 = CosNode("random string")
        cos2 = CosNode("random string")
        cos3 = CosNode("random string")
        cos1.assign_child([con1])
        cos1.calculate_value(1.1)
        cos2.assign_child([con2])
        cos2.calculate_value(1.1)
        cos3.assign_child([con4])
        cos3.calculate_value(1.1)
        self.assertEqual(cos1.value, math.cos(23.4))
        self.assertEqual(cos2.value, math.cos(2 * 1.1))
        self.assertEqual(cos3.value, math.cos(2.0 * math.pi))
        con4.value = None
        cos3.calculate_value(1.1)
        self.assertEqual(cos3.value, None)

    def test_ln(self):
        """
        Test ln node
        :return: nothing
        """
        con1, con2, con3, con4 = generate_cons()
        ln1 = LnNode("random string")
        ln2 = LnNode("random string")
        ln3 = LnNode("random string")
        ln1.assign_child([con1])
        ln1.calculate_value(1.1)
        ln2.assign_child([con2])
        ln2.calculate_value(1.1)
        ln3.assign_child([con4])
        ln3.calculate_value(1.1)
        self.assertEqual(ln1.value, math.log(23.4))
        self.assertEqual(ln2.value, math.log(2 * 1.1))
        self.assertEqual(ln3.value, math.log(2.0 * math.pi))

    def test_tan(self):
        """
        Test tan node
        :return: nothing
        """
        con1, con2, con3, con4 = generate_cons()
        tan1 = TanNode("random string")
        tan2 = TanNode("random string")
        tan3 = TanNode("random string")
        tan1.assign_child([con1])
        tan1.calculate_value(1.1)
        tan2.assign_child([con2])
        tan2.calculate_value(1.1)
        tan3.assign_child([con4])
        tan3.calculate_value(1.1)
        self.assertEqual(tan1.value, math.tan(23.4))
        self.assertEqual(tan2.value, math.tan(2 * 1.1))
        self.assertEqual(tan3.value, math.tan(2.0 * math.pi))

    def test_brace(self):
        """
        Test brace node
        :return: nothing
        """
        con1, con2, con3, con4 = generate_cons()
        brace1 = BraceNode(1, "random string")
        brace2 = BraceNode(1, "random string")
        brace3 = BraceNode(1, "random string")
        brace1.assign_child([con1])
        brace1.calculate_value(1.1)
        brace2.assign_child([con2])
        brace2.calculate_value(1.1)
        brace3.assign_child([con4])
        brace3.calculate_value(1.1)
        self.assertEqual(brace1.value, 23.4)
        self.assertEqual(brace2.value, (2 * 1.1))
        self.assertEqual(brace3.value, (2.0 * math.pi))

    def test_edge(self):
        """
        Test edge cases of ln and div
        :return:
        """
        con1, con2, con3, con4 = generate_cons()
        con5 = ConsNode("0.0")
        con5.calculate_value(1.8)
        div1 = DivNode("random string")
        div1.assign_child([con1, con5])
        div1.calculate_value(1.1)
        self.assertEqual(div1.value, None)
        ln1 = LnNode("random string")
        ln1.assign_child([con5])
        ln1.calculate_value(1.4)
        self.assertEqual(ln1.value, None)

    def test_mix(self):
        """
        Test mix of nodes
        :return: nothing
        """
        con1, con2, con3, con4 = generate_cons()
        div1 = DivNode("random string")
        div1.assign_child([con1, con2])
        div1.calculate_value(1.1)
        plus1 = PlusNode("random string")
        plus1.assign_child([div1, con3])
        plus1.calculate_value(1.1)
        tan1 = TanNode("random string")
        tan1.assign_child([con4])
        tan1.calculate_value(1.1)
        pow1 = PowerNode(1, "random string")
        pow1.assign_child([plus1, tan1])
        pow1.calculate_value(1.1)
        final = BraceNode(1, "random string")
        final.assign_child([pow1])
        final.calculate_value(1.1)
        self.assertEqual(final.value, (23.4 / (2 * 1.1) + math.pi) ** (math.tan(2.0 * math.pi)))

    def test_none(self):
        con1, con2, con3, con4 = generate_cons()
        con1.value = None
        con2.value = None
        con3.value = None
        con4.value = None
        div1 = DivNode("random string")
        div1.assign_child([con1, con2])
        div1.calculate_value(1.1)
        plus1 = PlusNode("random string")
        plus1.assign_child([div1, con3])
        plus1.calculate_value(1.1)
        tan1 = TanNode("random string")
        tan1.assign_child([con4])
        tan1.calculate_value(1.1)
        pow1 = PowerNode(1, "random string")
        pow1.assign_child([plus1, tan1])
        pow1.calculate_value(1.1)
        final = BraceNode(1, "random string")
        final.assign_child([pow1])
        final.calculate_value(1.1)
        self.assertEqual(final.value, None)

        div1 = MulNode("random string")
        div1.assign_child([con1, con2])
        div1.calculate_value(1.1)
        plus1 = MinusNode("random string")
        plus1.assign_child([div1, con3])
        plus1.calculate_value(1.1)
        tan1 = SinNode("random string")
        tan1.assign_child([con4])
        tan1.calculate_value(1.1)
        pow1 = DivNode("random string")
        pow1.assign_child([plus1, tan1])
        pow1.calculate_value(1.1)
        final = BraceNode(1, "random string")
        final.assign_child([pow1])
        final.calculate_value(1.1)
        self.assertEqual(final.value, None)


if __name__ == '__main__':
    unittest.main()
