import unittest
import os
import sys

from base_custom_comparison_sort_test import BaseCustomComparisonSortTest
from base_positive_integer_sort_test import BasePositiveIntegerSortTest
from base_negative_integer_sort_test import BaseNegativeIntegerSortTest
from base_string_sort_test import BaseStringSortTest

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'sort'))
import bubble_sort_optimised

class BubbleSortOptimisedTest(unittest.TestCase,
                              BaseCustomComparisonSortTest,
                              BasePositiveIntegerSortTest,
                              BaseNegativeIntegerSortTest,
                              BaseStringSortTest):
  def setUp(self):
    self.sort = bubble_sort_optimised.sort

if __name__ == '__main__':
  unittest.main()
