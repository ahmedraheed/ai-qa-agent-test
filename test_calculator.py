import unittest
from calculator import add, subtract, multiply, divide, sqrt

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_sqrt(self):
        self.assertEqual(sqrt(9), 3.0)
        self.assertEqual(sqrt(0), 0.0)
        self.assertEqual(sqrt(2.25), 1.5)
        with self.assertRaises(ValueError):
            sqrt(-1)

if __name__ == '__main__':
    unittest.main()
