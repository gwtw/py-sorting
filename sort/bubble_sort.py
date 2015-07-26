# py-sorting <http://github.com/GrowingWithTheWeb/py-sorting>
# Copyright 2015 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/GrowingWithTheWeb/py-sorting/blob/master/LICENSE>

from common.helpers import swap
from common.helpers import default_compare

def sort(list, compare=default_compare):
  for i in range(0, len(list) - 1):
    for j in range(1, len(list) - i):
      if compare(list[j - 1], list[j]) > 0:
        swap(list, j, j - 1);
  return list
