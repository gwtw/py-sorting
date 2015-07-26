# py-sorting <http://github.com/GrowingWithTheWeb/py-sorting>
# Copyright 2015 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/GrowingWithTheWeb/py-sorting/blob/master/LICENSE>

from common.helpers import compare as default_compare

def sort(list, compare=default_compare):
  for i in range(1, len(list)):
    item = list[i]
    indexHole = i
    while indexHole > 0 and compare(list[indexHole - 1], item) > 0:
      list[indexHole] = list[indexHole - 1]
      indexHole -= 1
    list[indexHole] = item
  return list
