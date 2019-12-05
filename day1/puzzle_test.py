from .puzzle import *
import unittest


class MyTestCase(unittest.TestCase):
    p = Puzzle('day1/input.txt')

    def test_calc_fuel(self):
        self.assertEqual(self.p.calc_fuel(654), 966)

    def test_part1(self):
        self.assertEqual(self.p.solve_part1(), 3325342)

    def test_part2(self):
        self.assertEqual(self.p.solve_part2(), 4985158)


if __name__ == '__main__':
    unittest.main()
