from fractions import Fraction
import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
    
## The test results show that the sum of the fraction do not equal 1 which cause the failure.
## It looks for the 2 equal numbers in the fraction (9,10). The (result,1) looks for the fraction to equal 1.
## The test see Fraction (9,10) and compares it to the (result,1) and determines it doesnt equal 1 causing a error.