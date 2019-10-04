import unittest
from .app import StockProfit


class StockProfitTest(unittest.TestCase):
    def setUp(self):
        self.tester = StockProfit()

    def test_case_1(self):
        payload = [7, 1, 5, 3, 6, 4]
        exp = 5
        self.assertEqual(self.tester.function(payload), exp)

    def test_case_2(self):
        payload = [7, 6, 4, 3, 1]
        exp = 0
        self.assertEqual(self.tester.function(payload), exp)
