import unittest
from parameterized import parameterized, parameterized_class
from src.FizzBuzz import *

class FizzBuzzParameterizedPackage(unittest.TestCase):
    def setUp(self):
        self.temp = FizzBuzz()

    @parameterized.expand([
        (5, "Buzz"),
        (3, "Fizz"),
        (15, "FizzBuzz"),
        (5.0, "Buzz"),
        (3.0, "Fizz"),
        (15.0, "FizzBuzz"),
        (5555, "Buzz"),
        (3333, "Fizz"),
        (15555, "FizzBuzz"),
    ])
    def test_one_parameterized(self,number, expected):
        self.assertEqual(self.temp.game(number), expected)


@parameterized_class(('number', 'expected'), [
    (5, "Buzz"),
    (3, "Fizz"),
    (15, "FizzBuzz"),
    (5.0, "Buzz"),
    (3.0, "Fizz"),
    (15.0, "FizzBuzz"),
    (5555, "Buzz"),
    (3333, "Fizz"),
    (15555, "FizzBuzz"),
])
class FizzBuzzParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.temp = FizzBuzz()

    def test_second_parameterized(self):
        self.assertEqual(self.temp.game(self.number), self.expected)


if __name__ == '__main__':
    unittest.main()
