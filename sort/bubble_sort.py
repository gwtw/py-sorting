# py-sorting <http://github.com/Tyriar/py-sorting>
# Copyright 2015 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/Tyriar/py-sorting/blob/master/LICENSE>

def default_compare(a, b):
  if a < b:
    return -1
  elif a > b:
    return 1
  return 0

def sort(list, compare=default_compare):
  for i in range(0, len(list) - 1):
    for j in range(1, len(list) - i):
      if compare(list[j - 1], list[j]) > 0:
        swap(list, j, j - 1);
  return list

def swap(list, a, b):
  temp = list[a]
  list[a] = list[b]
  list[b] = temp
