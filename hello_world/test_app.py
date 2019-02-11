import unittest
from .app import HelloWorld

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.name = 'shawnkoon'
        self.obj = HelloWorld(self.name)

    def test_local_variable(self):
        self.assertEqual(self.obj.name, self.name)

    def test_say_method(self):
        result_str = 'Hello World'
        self.assertEqual(self.obj.say(), result_str)
