import unittest

# make sure pycharm does not remove the import on auto format
# noinspection PyUnresolvedReferences
from context import mylib
from mylib import compute


class TestCount(unittest.TestCase):
    def test_add(self):
        self.assertEqual(compute.count.add(1, 2), 3)

    def test_mult(self):
        self.assertEqual(compute.count.mult(1, 2), 2)


class TestFunc(unittest.TestCase):
    def test_reduce_add(self):
        self.assertEqual(compute.functional.reduce_add((1, 2)), 3)

    def test_reduce_mult(self):
        self.assertEqual(compute.functional.reduce_mult((1, 2, 3)), 6)


if __name__ == '__main__':
    unittest.main()
