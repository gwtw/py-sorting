import unittest
import os
import sys

from base_positive_integer_sort_test import BasePositiveIntegerSortTest

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'sort'))
import counting_sort

class CountingSortTest(unittest.TestCase,
                       BasePositiveIntegerSortTest):
  def setUp(self):
    self.sort = counting_sort.sort

if __name__ == '__main__':
  unittest.main()
