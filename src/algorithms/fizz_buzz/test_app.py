import unittest
from .app import FizzBuzz


class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.tester = FizzBuzz()

    def test_case_1(self):
        payload = 15
        exp = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz"
        ]
        self.assertListEqual(self.tester.fizzBuzz(payload), exp)
