import unittest
from unittest import TestCase, mock
from simple_function import simple_function


class TestSimpleMethods(unittest.TestCase):
	
	@mock.patch.dict('os.environ', {'DATABASE_URL': 'myDatabase'})
	def test_true_return(self):
		self.assertEqual(simple_function(5), 5)

	def test_exception(self):
 		self.assertRaises(Exception, simple_function(5))

if __name__ == '__main__':
    unittest.main()