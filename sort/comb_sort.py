# py-sorting <http://github.com/GrowingWithTheWeb/py-sorting>
# Copyright 2015 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/GrowingWithTheWeb/py-sorting/blob/master/LICENSE>

import math

from common.helpers import swap
from common.helpers import default_compare

def sort(list, compare=default_compare):
  gap = len(list);
  shrinkFactor = 1.3;
  swapped = False;

  while gap > 1 or swapped:
    if gap > 1:
      gap = math.floor(gap / shrinkFactor)
    swapped = False;
    i = 0
    for i in range(len(list) - gap):
      if compare(list[i], list[i + gap]) > 0:
        swap(list, i, i + gap);
        swapped = True;
      i += 1

  return list;
