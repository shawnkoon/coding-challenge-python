import unittest
from .app import BestStockProfit2


class BestStockProfit2Test(unittest.TestCase):
    def setUp(self):
        self.tester = BestStockProfit2()

    def test_case_1(self):
        payload = [7, 1, 5, 3, 6, 4]
        exp = 7
        self.assertEqual(self.tester.function(payload), exp)

    def test_case_2(self):
        payload = [1, 2, 3, 4, 5]
        exp = 4
        self.assertEqual(self.tester.function(payload), exp)

    def test_case_3(self):
        payload = [5, 4, 3, 2, 1]
        exp = 0
        self.assertEqual(self.tester.function(payload), exp)
