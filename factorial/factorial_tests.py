import unittest
from factorial import factorial

class TestFactorialMethods(unittest.TestCase):

    def test_true_factorial(self):
        self.assertEqual(factorial(5), 120)

if __name__ == '__main__':
    unittest.main()