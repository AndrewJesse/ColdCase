import unittest
from learn_pandas.binomial_distribution import factorial, combination, binomial_distribution

class TestBinomialDistribution(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_combination(self):
        self.assertEqual(combination(5, 2), 10)
        self.assertEqual(combination(5, 0), 1)

    def test_binomial_distribution(self):
        self.assertAlmostEqual(binomial_distribution(5, 2, 0.5), 0.3125)
        self.assertAlmostEqual(binomial_distribution(5, 5, 0.5), 0.03125)

if __name__ == '__main__':
    unittest.main()