# py-sorting <http://github.com/GrowingWithTheWeb/py-sorting>
# Copyright 2015 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/GrowingWithTheWeb/py-sorting/blob/master/LICENSE>

from common.helpers import swap
from common.helpers import default_compare

def sort(array, compare=default_compare):
  for i in range(0, len(array)):
    minIndex = i
    for j in range(i + 1, len(array)):
      if compare(array[j], array[minIndex]) < 0:
        minIndex = j
    if minIndex != i:
      swap(array, i, minIndex)
  return array
