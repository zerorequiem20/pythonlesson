import unittest

def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
    return sum

class TestCountMethod(unittest.TestCase):

    def test_count(self):
        # Test case 1: Testing with list of integers
        self.assertEqual(count([1, 2, 3, 4, 5, 5, 5], 5), 3)

        # Test case 2: Testing with list of strings
        self.assertEqual(count(['a', 'b', 'a', 'c', 'a'], 'a'), 3)

        # Test case 3: Testing with empty list
        self.assertEqual(count([], 1), 0)

        # Test case 4: Testing with item not in sequence
        self.assertEqual(count([1, 2, 3, 4, 5], 6), 0)

        # Test case 5: Testing with sequence and item as None
        self.assertEqual(count([None, None, None], None), 3)

if __name__ == '__main__':
    unittest.main()
