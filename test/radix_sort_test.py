import unittest
import os
import sys

from base_negative_integer_sort_test import BaseNegativeIntegerSortTest
from base_positive_integer_sort_test import BasePositiveIntegerSortTest

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'sort'))
import radix_sort

class RadixSortTest(unittest.TestCase,
                    BasePositiveIntegerSortTest,
                    BaseNegativeIntegerSortTest):
  def setUp(self):
    self.sort = radix_sort.sort

if __name__ == '__main__':
  unittest.main()
