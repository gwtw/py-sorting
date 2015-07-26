# py-sorting <http://github.com/GrowingWithTheWeb/py-sorting>
# Copyright 2015 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/GrowingWithTheWeb/py-sorting/blob/master/LICENSE>

from common.helpers import swap
from common.helpers import default_compare

def sort(list, compare=default_compare):
  pos = 1;

  while pos < len(list):
    if compare(list[pos], list[pos - 1]) >= 0:
      pos += 1
    else:
      swap(list, pos, pos - 1)
      if pos > 1:
        pos -= 1;

  return list;
