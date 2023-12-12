import unittest
import math

def findAverage(num_values, values):
    total = sum(values)
    average = total / num_values
    return math.floor(average)

class TestFindAverage(unittest.TestCase):
    def test_average_integer_values(self):
        values = [1, 2, 3, 4, 5]
        result = findAverage(len(values), values)
        self.assertEqual(result, 3)  

    def test_average_float_values(self):
        values = [1.5, 2.5, 3.5]
        result = findAverage(len(values), values)
        self.assertEqual(result, 2)

    def test_average_single_value(self):
        values = [10]
        result = findAverage(len(values), values)
        self.assertEqual(result, 10)

    def test_average_all_same(self):
        values = [3, 3, 3]
        result = findAverage(len(values), values)
        self.assertEqual(result, 3)

    def test_average_negative_values(self):
        values = [-1, -2, -3, -4, -5]
        result = findAverage(len(values), values)
        self.assertEqual(result, -3) 

    def test_average_mixed_values(self):
        values = [5, 7, -2, 10, 3.5]
        result = findAverage(len(values), values)
        self.assertEqual(result, 4) 

if __name__ == '__main__':
    unittest.main()
