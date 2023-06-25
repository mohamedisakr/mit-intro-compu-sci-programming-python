from functools import lru_cache


@lru_cache(maxsize=100)
def factorial(n):
    """Calculates the factorial of a non-negative integer n.

    The factorial of n is defined as the product of all positive integers from 1 to n.
    For example, factorial(5) = 5 * 4 * 3 * 2 * 1 = 120.

    Note: n must be an integer.

    Args:
      n (int): The non-negative integer to calculate the factorial of.

    Returns:
      int: The factorial of n.

    Raises:
      ValueError: If n is negative.
      TypeError: If n is not an integer.
    """
    # check if n is an iteger
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    # check if n is negative
    if n < 0:
        raise ValueError("n must be non-negative")

    # base case: n is 0 or 1
    if n <= 1:
        return 1

    # recursive case: n is greater than 1
    else:
        return n * factorial(n - 1)
