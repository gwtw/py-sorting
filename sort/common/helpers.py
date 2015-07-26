# py-sorting <http://github.com/GrowingWithTheWeb/py-sorting>
# Copyright 2015 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/GrowingWithTheWeb/py-sorting/blob/master/LICENSE>

def default_compare(a, b):
  if a < b:
    return -1
  elif a > b:
    return 1
  return 0

def swap(list, a, b):
  temp = list[a]
  list[a] = list[b]
  list[b] = temp
