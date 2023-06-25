"""
Computes the nth Fibonacci number recursively
"""
from functools import lru_cache


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


# memo = {1: 1, 2: 1}
memo = {}


def fib_efficient(n):
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

    if n in memo:
        return memo[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fib_efficient(n-1) + fib_efficient(n-2)

    memo[n] = value  # fib_efficient(n-1) + fib_efficient(n-2)
    return value


# d = {1:1, 2:2}
# print(fib_efficient(6))
# print(memo)

# for i in range(1, 101):
#     print(f'{i} : {fib_efficient(i)}')

@lru_cache(maxsize=1000)
def fib_cache(n):
    """Computes the nth Fibonacci number recursively with .

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

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib_cache(n-1) + fib_cache(n-2)
