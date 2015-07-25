# py-sorting <http://github.com/GrowingWithTheWeb/py-sorting>
# Copyright 2015 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/GrowingWithTheWeb/py-sorting/blob/master/LICENSE>

from common.helpers import swap
from common.helpers import compare as default_compare

def sort(list, compare=default_compare):
  for i in range(0, len(list)):
    minIndex = i
    for j in range(i + 1, len(list)):
      if compare(list[j], list[minIndex]) < 0:
        minIndex = j
    if minIndex != i:
      swap(list, i, minIndex)
  return list
