import unittest
from password import PasswordStrengthChecker

class TestPasswordStrengthChecker(unittest.TestCase):
  def setUp(self):
    self.checker = PasswordStrengthChecker()

  def test_weak_pass(self):
    password = "weak"
    self.assertEqual(self.checker.check_pass_strength(password), 'very weak')

  def test_medium_pass(self):
    password = "heL!o"
    self.assertEqual(self.checker.check_pass_strength(password), 'medium')
  
  def test_strong_pass(self):
    password = "heL!o1"
    self.assertEqual(self.checker.check_pass_strength(password), 'strong')

  def test_very_strong_pass(self):
    password = "heL!o12345!"
    self.assertEqual(self.checker.check_pass_strength(password), 'very strong')

if __name__ == "__main__":
    unittest.main()
