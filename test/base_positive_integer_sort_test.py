class BasePositiveIntegerSortTest(object):
  def test_sorts_empty_array(self):
    self.assertEqual([], self.sort([]))

  def test_sorts_small_sorted_array(self):
    self.assertEqual([1,2,3,4,5], self.sort([1,2,3,4,5]))

  def test_sorts_small_reverse_sorted_array(self):
    self.assertEqual([1,2,3,4,5], self.sort([5,4,3,2,1]))

  def test_sorts_small_sorted_array_with_two_values_swapped(self):
    self.assertEqual([1,2,3,4,5], self.sort([1,2,5,4,3]))

  def test_sorts_large_sorted_array(self):
    self.assertEqual(
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        self.sort([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))

  def test_sorts_large_reverse_sorted_array(self):
    self.assertEqual(
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        self.sort([20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]))

  def test_sorts_large_sorted_array_with_two_values_swapped(self):
    self.assertEqual(
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        self.sort([0,1,2,8,4,5,6,7,3,9,10,11,12,13,14,15,16,17,18,19,20]))
