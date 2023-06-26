from unittest import TestCase, main
from oop.fraction import Fraction


class TestFraction(TestCase):
    """A class for testing the Fraction class"""

    def test_init(self):
        """Test the __init__ method"""
        f1 = Fraction(1, 2)
        self.assertEqual(f1.num, 1)
        self.assertEqual(f1.denom, 2)

        f2 = Fraction(-3, 4)
        self.assertEqual(f2.num, -3)
        self.assertEqual(f2.denom, 4)

    def test_init_type_error_float(self):
        """Test the fraction method for type errors."""
        with self.assertRaises(TypeError):
            f3 = Fraction(1.5, 2)

    def test_init_type_error_string(self):
        """Test the fraction method for type errors."""
        with self.assertRaises(TypeError):
            f4 = Fraction(1, "2")

    def test_init_type_error_array(self):
        """Test the fraction method for type errors."""
        with self.assertRaises(TypeError):
            f4 = Fraction(1, [10, 20])

    def test_repr(self):
        """Test the __repr__ method"""
        f1 = Fraction(1, 2)
        self.assertEqual(repr(f1), "1 / 2")

        f2 = Fraction(-3, 4)
        self.assertEqual(repr(f2), "-3 / 4")

    def test_add(self):
        """Test the __add__ method"""
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        f3 = f1 + f2
        self.assertEqual(f3.num, 10)
        self.assertEqual(f3.denom, 8)

    def test_sub(self):
        """Test the __sub__ method"""
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        f3 = f1 - f2
        self.assertEqual(f3.num, -2)
        self.assertEqual(f3.denom, 8)

    def test_float(self):
        """Test the __float__ method"""
        f1 = Fraction(1, 2)
        self.assertEqual(float(f1), 0.5)

        f2 = Fraction(-3, 4)
        self.assertEqual(float(f2), -0.75)

    def test_inverse(self):
        """Test the inverse method"""
        f1 = Fraction(1, 2)
        f2 = f1.inverse()
        self.assertEqual(f2.num, 2)
        self.assertEqual(f2.denom, 1)


if __name__ == "__main__":
    main()
