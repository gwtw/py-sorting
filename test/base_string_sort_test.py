class BaseStringSortTest(object):
  def test_sorts_sorted_character_array(self):
    self.assertEqual(["a","b","c","d","e"], self.sort(["a","b","c","d","e"]))
    
  def test_sorts_reverse_sorted_character_array(self):
    self.assertEqual(["a","b","c","d","e"], self.sort(["e","d","c","b","a"]))
    
  def test_sorts_sorted_character_array_with_two_values_swapped(self):
    self.assertEqual(["a","b","c","d","e"], self.sort(["a","c","b","d","e"]))
    
  def test_sorts_jumbled_character_array(self):
    self.assertEqual(
        ["a","b","c","d","e","f","g","h","i","j"],
        self.sort(["i","b","a","h","c","g","d","f","e","j"]))
    
  def test_sorts_character_array_with_duplicate_values(self):
    self.assertEqual(
        ["a","a","b","b","c","c","d","d"],
        self.sort(["b","c","a","d","c","a","b","d"]))
    
  def test_sorts_sorted_string_array(self):
    self.assertEqual(
        ["aa","bb","cc","dd","ee"],
        self.sort(["aa","bb","cc","dd","ee"]))
    
  def test_sorts_reverse_sorted_string_array(self):
    self.assertEqual(
        ["aa","bb","cc","dd","ee"],
        self.sort(["ee","dd","cc","bb","aa"]))
    
  def test_sorts_sorted_string_array_with_two_values_swapped(self):
    self.assertEqual(
        ["aa","bb","cc","dd","ee"],
        self.sort(["aa","cc","bb","dd","ee"]))
    
  def test_sorts_jumbled_string_array(self):
    self.assertEqual(
        ["aa","bb","cc","dd","ee","ff","gg","hh","ii","jj"], 
        self.sort(["ii","bb","aa","hh","cc","gg","dd","ff","ee","jj"]))
    
  def test_sorts_string_array_with_duplicate_values(self):
    self.assertEqual(
        ["aa","aa","bb","bb","cc","cc","dd","dd"], 
        self.sort(["bb","cc","aa","dd","cc","aa","bb","dd"]))
    
  def test_sorts_second_character_in_a_string_array(self):
    self.assertEqual(
        ["aa","ab","ba","bb","ca","cb","da","db"], 
        self.sort(["bb","ca","ab","da","cb","aa","ba","db"]))
