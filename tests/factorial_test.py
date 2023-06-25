from unittest import TestCase, main
from recursion_dictionaries.factorial import factorial

# define a test class that inherits from unittest.TestCase


class TestFactorial(TestCase):

    # define a test method for test case 1: n is a positive integer less than or equal to 20
    def test_positive_small(self):
        # use assertEqual to check if the expected and actual outputs are equal
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(20), 2432902008176640000)

    # define a test method for test case 2: n is a negative integer
    # def test_negative(self):
    #     # use assertRaises to check if the function raises a ValueError with a negative argument
    #     self.assertRaises(ValueError, factorial, -3)
    #     self.assertRaises(ValueError, factorial, -10)

# my code
    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_fib_non_integer(self):
        with self.assertRaises(TypeError):
            factorial(1.5)

    # define a test method for test case 3: n is zero or one
    def test_zero_one(self):
        # use assertEqual to check if the expected and actual outputs are equal
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    # define a test method for test case 4: n is a positive integer greater than 20
    def test_positive_large(self):
        # use assertEqual to check if the expected and actual outputs are equal
        self.assertEqual(factorial(21), 51090942171709440000)
        self.assertEqual(factorial(30), 265252859812191058636308480000000)


# run the tests
if __name__ == "__main__":
    main()
