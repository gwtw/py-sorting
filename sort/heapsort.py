# py-sorting <http://github.com/GrowingWithTheWeb/py-sorting>
# Copyright 2015 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/GrowingWithTheWeb/py-sorting/blob/master/LICENSE>

import math

from common.helpers import swap
from common.helpers import default_compare

def sort(array, compare=default_compare):
  heap_size = len(array)
  build_heap(array, heap_size, compare)
  while heap_size > 1:
    heap_size -= 1
    swap(array, 0, heap_size)
    heapify(array, heap_size, 0, compare)
  return array

def heapify(array, heap_size, i, compare):
  left = i * 2 + 1
  right = i * 2 + 2
  largest = i
  if left < heap_size and compare(array[left], array[largest]) > 0:
    largest = left
  if right < heap_size and compare(array[right], array[largest]) > 0:
    largest = right
  if largest != i:
    swap(array, i, largest)
    heapify(array, heap_size, largest, compare)

def build_heap(array, heap_size, compare):
  for i in range(math.floor(len(array) / 2), -1, -1):
    heapify(array, heap_size, i, compare)
