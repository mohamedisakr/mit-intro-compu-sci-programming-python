"""
Fibonacci sequence test cases
"""
from unittest import TestCase, main
from recursion_dictionaries.fib import fibonacci


class TestFib(TestCase):

    def test_fib_0(self):
        self.assertEqual(fibonacci(0), 1)

    def test_fib_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fib_2(self):
        self.assertEqual(fibonacci(2), 2)

    def test_fib_3(self):
        self.assertEqual(fibonacci(3), 3)

    def test_fib_4(self):
        self.assertEqual(fibonacci(4), 5)

    def test_fib_5(self):
        self.assertEqual(fibonacci(5), 8)

    def test_fib_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_fib_non_integer(self):
        with self.assertRaises(TypeError):
            fibonacci(1.5)


if __name__ == '__main__':
    main()
