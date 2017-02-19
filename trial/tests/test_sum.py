import unittest, os, sys

#Please provide the absolute path of the location of source file
sys.path.append(os.path.abspath('../trial/src'))

from my_sum import add_integers

class TestSum(unittest.TestCase):
	"""docstring for TestSum"unittest.TestCasef __init__(self, arg):
		super TestSum,unittest.TestCase.__init__()

		self.arg = arg"""

	def test_sum(self):
		print "testing sum function"
		test_add_int = add_integers()
                #self.assertEqual(test_add_int.add_int([1,2]), 4)
		self.assertEqual(test_add_int.add_int([1,2]), 3)

if __name__ == '__main__':
    unittest.main()
