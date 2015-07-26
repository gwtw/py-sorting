# py-sorting <http://github.com/GrowingWithTheWeb/py-sorting>
# Copyright 2015 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/GrowingWithTheWeb/py-sorting/blob/master/LICENSE>

import math

from common.helpers import swap
from common.helpers import default_compare

def sort(list, compare=default_compare):
  start = -1
  end = len(list) - 2
  swapped = True
  while swapped:
    swapped = False
    for i in range(start + 1, end):
      if compare(list[i], list[i + 1]) > 0:
        swap(list, i, i + 1)
        swapped = True
    if not swapped:
      break
    swapped = False
    for i in range(end, start, -1):
      if compare(list[i], list[i + 1]) > 0:
        swap(list, i, i + 1)
        swapped = True
  return list;
