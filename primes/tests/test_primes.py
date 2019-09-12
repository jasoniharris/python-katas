import unittest2
from primes import is_prime

class PrimesTestCase(unittest2.TestCase):
    """Tests for `primes.py`."""

    def test_true_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(3))

    def test_false_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(12))

    def test_negative_number(self):
        """Is a negative number correctly determined not to be prime?"""
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-2))

if __name__ == '__main__':
    unittest2.main()