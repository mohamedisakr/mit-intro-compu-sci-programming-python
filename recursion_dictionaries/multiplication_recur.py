def mult_recur(a, b):
    """Computes the nth Fibonacci number recursively with .

    Args:
      n (int): The index of the Fibonacci number to compute.

    Returns:
      int: The nth Fibonacci number.

    Raises:
      ValueError: If n is negative.
      TypeError: If n is not an integer.
    """
    if not isinstance(a, int):
        raise TypeError("a must be an integer")

    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    if b < 0:
        raise ValueError("b must be non-negative")

    if b == 1:
        return a

    return a + mult_recur(a, b-1)


print(mult_recur(30, 50))
