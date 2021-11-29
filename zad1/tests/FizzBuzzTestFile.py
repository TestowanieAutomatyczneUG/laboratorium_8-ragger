from src.FizzBuzz import *
import unittest
import json
class FizzBuzzTest(unittest.TestCase):
    def test_from_sampleFile(self):
        sampleFile = open("./sampleFile.json")
        fizzBuzz = FizzBuzz()
        testData = json.load(sampleFile)
        for [input, expectedOutput] in testData:
            self.assertEqual(fizzBuzz.game(input), expectedOutput)


if __name__ == '__main__':
    unittest.main()
