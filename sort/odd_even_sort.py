# py-sorting <http://github.com/GrowingWithTheWeb/py-sorting>
# Copyright 2015 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/GrowingWithTheWeb/py-sorting/blob/master/LICENSE>

from common.helpers import swap
from common.helpers import default_compare

def sort(list, compare=default_compare):
  sorted = False
  while not sorted:
    sorted = inner_sort(list, 1, compare)
    sorted = sorted and inner_sort(list, 0, compare)
  return list

def inner_sort(list, start_i, compare):
  sorted = True
  for i in range(start_i, len(list) - 1, 2):
    if compare(list[i], list[i + 1]) > 0:
      swap(list, i, i + 1)
      sorted = False
  return sorted
