import unittest
from a_star import a_star

class AStarTestCase(unittest.TestCase):

    def test_case_1(self):
        inf_pitcher = 100000
        capacities = (inf_pitcher, 1, 4, 10, 15, 22)
        target = 181
        expected = 20
        self.assertEqual(a_star(capacities, target), expected)

    def test_case_2(self):
        inf_pitcher = 100000
        capacities = (inf_pitcher, 2, 5, 6, 72)
        target = 143
        expected = 7
        self.assertEqual(a_star(capacities, target), expected)

    def test_case_3(self):
        inf_pitcher = 100000
        capacities = (inf_pitcher, 3, 6)
        target = 2
        expected = -1
        self.assertEqual(a_star(capacities, target), expected)

    def test_case_4(self):
        inf_pitcher = 100000
        capacities = (inf_pitcher, 2)
        target = 143
        expected = -1
        self.assertEqual(a_star(capacities, target), expected)

    def test_case_5(self):
        inf_pitcher = 100000
        capacities = (inf_pitcher, 2, 3, 5, 19, 121, 852)
        target = 11443
        expected = 36
        self.assertEqual(a_star(capacities, target), expected)

