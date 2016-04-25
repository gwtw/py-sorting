import unittest
import os
import sys

from base_custom_comparison_sort_test import BaseCustomComparisonSortTest
from base_integer_sort_test import BaseIntegerSortTest
from base_string_sort_test import BaseStringSortTest

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'sort'))
import heapsort

class HeapsortSortTest(unittest.TestCase,
                       BaseCustomComparisonSortTest,
                       BaseIntegerSortTest,
                       BaseStringSortTest):
  def setUp(self):
    self.sort = heapsort.sort

if __name__ == '__main__':
  unittest.main()
