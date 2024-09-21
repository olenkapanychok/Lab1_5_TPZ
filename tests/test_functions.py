import unittest
from main import (add_elements, subtract, multiply, divide, integer_division,
                  modulus, factorial, abs_value, max_in_list, concatenate_strings,
                  find_substring)

class TestFunctions(unittest.TestCase):

    def test_add_elements(self):
        self.assertEqual(add_elements([1, 2, 3]), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_integer_division(self):
        self.assertEqual(integer_division(10, 3), 3)
        with self.assertRaises(ValueError):
            integer_division(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        with self.assertRaises(ValueError):
            modulus(10, 0)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_abs_value(self):
        self.assertEqual(abs_value(-5), 5)

    def test_max_in_list(self):
        self.assertEqual(max_in_list([1, 2, 3]), 3)
        with self.assertRaises(ValueError):
            max_in_list([])

    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings("hello", "world"), "helloworld")

    def test_find_substring(self):
        self.assertEqual(find_substring("hello world", "world"), 6)
        self.assertEqual(find_substring("hello world", "python"), -1)

if __name__ == '__main__':
    unittest.main()
