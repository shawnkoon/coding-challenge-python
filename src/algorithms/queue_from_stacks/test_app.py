import unittest
from .app import QueueFromStacks


class QueueFromStacksTest(unittest.TestCase):
    def setUp(self):
        self.queue = QueueFromStacks()

    def test_case_1(self):
        test_val1 = 32
        test_val2 = 124

        self.assertTrue(self.queue.empty(), 'Queue should be empty at first.')

        self.queue.push(test_val1)
        self.queue.push(test_val2)
        self.assertFalse(self.queue.empty(),
                         'Queue should be NOT empty after push.')

        self.assertEquals(self.queue.peek(), test_val1,
                          'Queue should correctly return top value on peek.')

        self.assertEquals(self.queue.pop(), test_val1,
                          'Queue should correctly return top value on pop.')
