'''test for interface's output'''
import unittest
import numpy
from plotter.interface_output import plotter, shifter,plotting


class MyTestCase(unittest.TestCase):
    
    def test_interface(self):
        '''testing results'''
        #img = numpy.ones((500,500,1),numpy.uint8)*255
        img_after=plotter([[0.5,0.5],[0.5,-0.5]],[-1,1],[-1,1],"test")
        p1 = shifter([0.5,0.5],[-1,1],[-1,1])
        p2 = shifter([0.5,-0.5],[-1,1],[-1,1])
        assert img_after[p1[1]][p1[0]] <= 1
        assert img_after[p2[1]][p2[0]] <= 1
        assert img_after[250][250] <= 1
    
    def test_coordinate(self):
        '''testing coordinates'''
        p1 = shifter([0.5,0.5],[-1,1],[-1,1])
        p2 = shifter([0.5,-0.5],[-1,1],[-1,1])
        assert p2[1] == 500-p1[1]
        assert p2[0] == p1[0]

    def test_line(self):
        img = plotting("x",[-1,1],[-1,1])
        assert img[250][250] <= 1
        assert img[100][400] <= 1
        assert img[1][250] <= 1
        assert img[250][499] <= 1

if __name__ == '__main__':
    unittest.main()
