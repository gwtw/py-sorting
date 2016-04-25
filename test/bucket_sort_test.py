import unittest
import os
import sys

from base_positive_integer_sort_test import BasePositiveIntegerSortTest
from base_negative_integer_sort_test import BaseNegativeIntegerSortTest

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'sort'))
import bucket_sort

class BucketSortTest(unittest.TestCase,
                     BasePositiveIntegerSortTest,
                     BaseNegativeIntegerSortTest):
  def setUp(self):
    self.sort = bucket_sort.sort

if __name__ == '__main__':
  unittest.main()
