# py-sorting <http://github.com/GrowingWithTheWeb/py-sorting>
# Copyright 2015 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/GrowingWithTheWeb/py-sorting/blob/master/LICENSE>

from common.helpers import swap
from common.helpers import default_compare

def sort(array, compare=default_compare):
  sorted = False
  while not sorted:
    sorted = inner_sort(array, 1, compare)
    sorted = sorted and inner_sort(array, 0, compare)
  return array

def inner_sort(array, start_i, compare):
  sorted = True
  for i in range(start_i, len(array) - 1, 2):
    if compare(array[i], array[i + 1]) > 0:
      swap(array, i, i + 1)
      sorted = False
  return sorted
