# py-sorting <http://github.com/GrowingWithTheWeb/py-sorting>
# Copyright 2015 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/GrowingWithTheWeb/py-sorting/blob/master/LICENSE>

import common.helpers as helpers

def sort(list, compare=helpers.compare):
  unsorted_below = len(list)
  while unsorted_below != 0:
    last_swap = 0
    for i in range(1, unsorted_below):
      if compare(list[i - 1], list[i]) > 0:
        helpers.swap(list, i, i - 1);
        last_swap = i
    unsorted_below = last_swap
  return list
