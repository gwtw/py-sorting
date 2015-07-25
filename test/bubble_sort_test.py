import unittest
import os
import sys

from base_integer_sort_test import BaseIntegerSortTest
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'sort'))
import bubble_sort

class BubbleSortTest(unittest.TestCase, BaseIntegerSortTest):
    def setUp(self):
        self.sort = bubble_sort.sort

if __name__ == '__main__':
    unittest.main()
