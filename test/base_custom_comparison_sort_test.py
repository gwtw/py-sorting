def reverse_compare(a, b):
  if a < b:
    return 1
  elif a > b:
    return -1
  return 0

class BaseCustomComparisonSortTest(object):
  def test_custom_compare_sorts_empty_array(self):
    self.assertEqual([], self.sort([], reverse_compare))

  def test_custom_compare_sorts_small_sorted_array(self):
    self.assertEqual([5,4,3,2,1], self.sort([1,2,3,4,5], reverse_compare))

  def test_custom_compare_sorts_small_reverse_sorted_array(self):
    self.assertEqual([5,4,3,2,1], self.sort([5,4,3,2,1], reverse_compare))

  def test_custom_compare_sorts_small_negative_only_sorted_array(self):
    self.assertEqual([-1,-2,-3,-4,-5], self.sort([-5,-4,-3,-2,-1], reverse_compare))

  def test_custom_compare_sorts_small_negative_only_reverse_sorted_array(self):
    self.assertEqual([-1,-2,-3,-4,-5], self.sort([-1,-2,-3,-4,-5], reverse_compare))

  def test_custom_compare_sorts_small_sorted_array_with_two_values_swapped(self):
    self.assertEqual([5,4,3,2,1], self.sort([1,2,5,4,3], reverse_compare))

  def test_custom_compare_sorts_large_sorted_array(self):
    self.assertEqual(
        [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0],
        self.sort([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], reverse_compare))

  def test_custom_compare_sorts_large_reverse_sorted_array(self):
    self.assertEqual(
        [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0],
        self.sort([20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0], reverse_compare))

  def test_custom_compare_sorts_large_sorted_array_with_two_values_swapped(self):
    self.assertEqual(
        [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0],
        self.sort([0,1,2,8,4,5,6,7,3,9,10,11,12,13,14,15,16,17,18,19,20], reverse_compare))

  def test_custom_compare_sorts_large_negative_only_sorted_array(self):
    self.assertEqual(
        [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20],
        self.sort([-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1], reverse_compare))

  def test_custom_compare_sorts_large_negative_only_reverse_sorted_array(self):
    self.assertEqual(
        [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20],
        self.sort([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20], reverse_compare))

  def test_custom_compare_sorts_large_jumbled_small_range_array(self):
    self.assertEqual(
        [5,4,3,2,1,0,-1,-2,-3,-4,-5],
        self.sort([5,-3,2,0,-5,1,4,-4,-2,3,-1], reverse_compare))

  def test_custom_compare_sorts_large_jumbled_large_range_array(self):
    self.assertEqual(
        [2938,523,108,102,16,10,-38,-50,-4011],
        self.sort([102,10,-50,2938,108,-4011,-38,523,16], reverse_compare))

  def test_custom_compare_sorts_duplicate_values(self):
    self.assertEqual(
        [10,9,1,1,-2,-2,-7,-7,-7,-7],
        self.sort([-2,-7,1,9,-7,1,-2,10,-7,-7], reverse_compare))
