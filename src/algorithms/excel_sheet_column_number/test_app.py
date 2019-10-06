import unittest
from .app import ExcelColumnNumber


class ExcelColumnNumberTest(unittest.TestCase):
    def setUp(self):
        self.tester = ExcelColumnNumber()

    def test_case_1(self):
        payload = "A"
        exp = 1
        self.assertEqual(self.tester.get_number(payload), exp)

    def test_case_2(self):
        payload = "XE"
        exp = 629
        self.assertEqual(self.tester.get_number(payload), exp)

    def test_case_3(self):
        payload = "JAZZ"
        exp = 177138
        self.assertEqual(self.tester.get_number(payload), exp)
