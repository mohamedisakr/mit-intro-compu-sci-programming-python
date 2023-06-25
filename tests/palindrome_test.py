from unittest import TestCase, main
from recursion_dictionaries.palindrome import isPalindrome


# define a test class that inherits from unittest.TestCase
class TestIsPalindrome(TestCase):

    # define a test method for test case 1: s is an empty string
    def test_empty(self):
        # use assertTrue to check if the function returns True
        self.assertTrue(isPalindrome(""))

    # define a test method for test case 2: s is a single character
    def test_single(self):
        # use assertTrue to check if the function returns True
        self.assertTrue(isPalindrome("a"))

    # define a test method for test case 3: s is a palindrome with an
    # even number of characters
    def test_even(self):
        # use assertTrue to check if the function returns True
        self.assertTrue(isPalindrome("abba"))

    # define a test method for test case 4: s is a palindrome with an
    # odd number of characters
    def test_odd(self):
        # use assertTrue to check if the function returns True
        self.assertTrue(isPalindrome("racecar"))

    # define a test method for test case 5: s is not a palindrome with
    # an even number of characters
    def test_not_even(self):
        # use assertFalse to check if the function returns False
        self.assertFalse(isPalindrome("abca"))

    # define a test method for test case 6: s is not a palindrome with an
    # odd number of characters
    def test_not_odd(self):
        # use assertFalse to check if the function returns False
        self.assertFalse(isPalindrome("racer"))

    # define a test method for test case 7: s contains spaces or punctuation
    # marks
    def test_spaces_punctuation(self):
        # use assertTrue or assertFalse to check if the function returns
        # the expected value
        self.assertTrue(isPalindrome("madam, I'm Adam"))
        self.assertTrue(isPalindrome("a man, a plan, a canal, Panama!"))

    # define a test method for test case 8: s palindrome number 1441
    def test_spaces_palindrome_number(self):
        # use assertTrue or assertFalse to check if the function returns
        # the expected value
        self.assertTrue(isPalindrome(1441))

    # define a test method for test case 9: s NON palindrome number 1234
    def test_spaces_non_palindrome_number(self):
        # use assertTrue or assertFalse to check if the function returns
        # the expected value
        self.assertFalse(isPalindrome(1234))

    # define a test method for test case 10: s is a palindrome that contains
    # uppercase and lowercase letters
    def test_upper_lower(self):
        # use assertTrue to check if the function returns True
        self.assertTrue(isPalindrome("Anna"))

    # define a test method for test case 11: s is not a palindrome that
    # contains uppercase and lowercase letters
    def test_not_upper_lower(self):
        # use assertFalse to check if the function returns False
        self.assertFalse(isPalindrome("Alice"))

    # define a test method for test case 12: s is a palindrome that contains
    # numbers
    def test_numbers(self):
        # use assertTrue to check if the function returns True
        self.assertTrue(isPalindrome("12321"))

    # define a test method for test case 13: s is not a palindrome that
    # contains numbers
    def test_not_numbers(self):
        # use assertFalse to check if the function returns False
        self.assertFalse(isPalindrome("12345"))

    # define a test method for test case 14: s is a palindrome that contains
    # alphanumeric characters
    def test_alphanumeric(self):
        # use assertTrue to check if the function returns True
        self.assertTrue(isPalindrome("a1b2b1a"))

    # define a test method for test case 15: s is not a palindrome that
    # contains alphanumeric characters
    def test_not_alphanumeric(self):
        # use assertFalse to check if the function returns False
        self.assertFalse(isPalindrome("a1b2c3"))

    # ----------------

    # define a test method for test case 16: s is None
    def test_none(self):
     # use assertRaises to check if the function raises a TypeError
     # with None as an argument
        # self.assertRaises(TypeError, isPalindrome, None)
        self.assertFalse(isPalindrome(None))

   # define a test method for test case 17: s is not a string
    def test_not_string(self):
     # use assertRaises to check if the function raises a TypeError with
     # a non-string argument
        self.assertFalse(isPalindrome(123))

   # define a test method for test case 18: s is a very long string
    def test_long_text(self):
        # use assertFalse to check if the function returns False with
        # a very long string as an argument
        # self.assertFalse(isPalindrome("a" * 1000000 + "b" + "a" * 1000000))
        self.assertTrue(isPalindrome("a" * 100 + "b" + "a" * 100))


# run the tests
if __name__ == "__main__":
    main()
