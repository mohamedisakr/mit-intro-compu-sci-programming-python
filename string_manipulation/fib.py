"""
Computes the nth Fibonacci number recursively
"""


def fibonacci(n):
    """Computes the nth Fibonacci number recursively.

    Args:
      n (int): The index of the Fibonacci number to compute.

    Returns:
      int: The nth Fibonacci number.

    Raises:
      ValueError: If n is negative.
      TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
