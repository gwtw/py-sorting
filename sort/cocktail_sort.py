# py-sorting <http://github.com/GrowingWithTheWeb/py-sorting>
# Copyright 2015 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/GrowingWithTheWeb/py-sorting/blob/master/LICENSE>

import math

from common.helpers import swap
from common.helpers import default_compare

def sort(array, compare=default_compare):
  start = -1
  end = len(array) - 2
  swapped = True
  while swapped:
    swapped = False
    for i in range(start + 1, end):
      if compare(array[i], array[i + 1]) > 0:
        swap(array, i, i + 1)
        swapped = True
    if not swapped:
      break
    swapped = False
    for i in range(end, start, -1):
      if compare(array[i], array[i + 1]) > 0:
        swap(array, i, i + 1)
        swapped = True
  return array;
