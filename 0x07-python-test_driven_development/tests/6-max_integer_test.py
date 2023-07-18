import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 0, 10, -5, 5]), 10)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_string_elements(self):
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_mixed_elements(self):
        self.assertEqual(max_integer(["a", 1, "b", 2]), TypeError)

if __name__ == '__main__':
    unittest.main()
