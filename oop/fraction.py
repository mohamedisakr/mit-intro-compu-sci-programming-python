"""
 EXAMPLE: simple class to represent fractions
 Try adding more built-in operations like multiply, divide
 Try adding a reduce method to reduce the fraction (use gcd)
"""


class Fraction:
    """
    A number represented as a fraction
    """

    def __init__(self, num, denom):
        """Initialize the fraction with numerator and denomenator.

        Args:
            num (int): The numerator of the fraction.
            denom (int): The denomenator of the fraction.

        Raises:
            TypeError: If num or denom is not an int.
        """

        # check if num and denom are of type int.
        if not isinstance(num, int):
            raise TypeError(f"num must be an int, not {type(num)}")

        if not isinstance(denom, int):
            raise TypeError(f"denom must be an int, not {type(denom)}")

        # assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom

    def __repr__(self):  # __str__
        """ Retunrs a string representation of self """
        return f"{self.num} / {self.denom}"

    def __add__(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)

    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)

    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denom

    def inverse(self):
        """ Returns a new fraction representing 1/self """
        return Fraction(self.denom, self.num)
