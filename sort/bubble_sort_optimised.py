# py-sorting <http://github.com/GrowingWithTheWeb/py-sorting>
# Copyright 2015 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/GrowingWithTheWeb/py-sorting/blob/master/LICENSE>

from common.helpers import swap
from common.helpers import default_compare

def sort(array, compare=default_compare):
  unsorted_below = len(array)
  while unsorted_below != 0:
    last_swap = 0
    for i in range(1, unsorted_below):
      if compare(array[i - 1], array[i]) > 0:
        swap(array, i, i - 1);
        last_swap = i
    unsorted_below = last_swap
  return array
