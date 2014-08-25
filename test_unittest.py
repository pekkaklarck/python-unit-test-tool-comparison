import unittest

from sut import compare


class TestCompare(unittest.TestCase):

    def test_x_greater_than_y_returns_1(self):
        for x, y in [(2, 1), (1, 0), (0, -1), (1.1, 1)]:
            self.assertEquals(compare(x, y), 1)

    def test_x_equal_to_y_returns_0(self):
        for x in [0, 1, -1, 1.1]:
            self.assertEquals(compare(x, x), 0)

    def test_x_less_than_y_returns_minus_1(self):
        for x, y in [(1, 2), (0, 1), (-1, 0), (1, 1.1)]:
            self.assertEquals(compare(x, y), -1)

    def test_failing(self):
        self.assertEquals(compare(1, 0), 0)


if __name__ == '__main__':
    unittest.main()

