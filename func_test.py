import math
import unittest

def convert_value(x):
    if x <= 2:
        y = 6.811 * (1 + math.exp(6.81 * x))
    else:
        y = math.sqrt(x + math.exp(-x)) 
    return y
# Лазарева Ольга Андреевна  , варинант 9, группа 44-22-114
class ConvertValueTestCase(unittest.TestCase):
    def test_x_less_than_2(self):
        result = convert_value(1)
        expected = 6.811 * (1 + math.exp(6.81 * 1))
        self.assertEqual(result, expected)

    def test_x_greater_than_2(self):
        result = convert_value(3)
        expected = math.sqrt(3 + math.exp(-3))
        self.assertEqual(result, expected)

    def test_x_equal_to_2(self):
        result = convert_value(2)
        expected = 6.811 * (1 + math.exp(6.81 * 2))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()