"""
Fibonacci sequence test cases
"""
from unittest import TestCase
from recursion_dictionaries.fib import fib_efficient


class TestFib(TestCase):

    # def test_fib_0(self):
    #     self.assertEqual(fib_efficient(0), 1)

    def test_fib_1(self):
        self.assertEqual(fib_efficient(1), 1)

    def test_fib_2(self):
        self.assertEqual(fib_efficient(2), 1)

    def test_fib_3(self):
        self.assertEqual(fib_efficient(3), 2)

    def test_fib_4(self):
        self.assertEqual(fib_efficient(4), 3)

    def test_fib_5(self):
        self.assertEqual(fib_efficient(5), 5)

    def test_fib_6(self):
        self.assertEqual(fib_efficient(6), 8)

    def test_fib_negative(self):
        with self.assertRaises(ValueError):
            fib_efficient(-1)

    def test_fib_non_integer(self):
        with self.assertRaises(TypeError):
            fib_efficient(1.5)


# if __name__ == '__main__':
#     main()
