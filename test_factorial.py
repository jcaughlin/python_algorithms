import unittest
import factorial


class Test_Factorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial.factorial(5), 120)
