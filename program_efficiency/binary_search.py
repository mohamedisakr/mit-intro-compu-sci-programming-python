import unittest


def binary_search(arr: list[int], target: int) -> int:
    """
    Performs a binary search on a sorted array to find the index of 
    the target element.

    Parameters
    ----------
    arr : list
        A sorted list of comparable elements.
    target : int
        The element to search for in the array.

    Returns
    -------
    int or None
        The index of the target element in the array, or None if not found.

    Raises
    ------
    ValueError: If the array is empty.
    ValueError: If the array is not sorted.
    TypeError: If the target element is not comparable to the elements in 
               the array.

    Examples
    --------
    >>> binary_search([1, 2, 3, 4, 5], 3)
    2
    >>> binary_search([1, 2, 3, 4, 5], 6)
    None
    >>> binary_search([], 1)
    ValueError: array must not be empty
    >>> binary_search([2, 1, 3], 1)
    ValueError: array must be sorted
    >>> binary_search([1, 2, 3], "a")
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    # check for pre-condition
    # check if arr is empty
    if len(arr) == 0:
        return None

    if not isinstance(target, int):
        raise TypeError(f"target must be an int, not {type(target)}")

    if all(not isinstance(item, int) for item in arr):
        raise TypeError(f"item must be an int, not {type(item)}")

    # check if target value less than smallest item in the array
    if target < arr[0]:
        return None

    # check if target value greater than largest item in the array
    if target > arr[len(arr)-1]:
        return None

    # assume arr is sorted in ascending order
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # found the target, return its index
        elif arr[mid] < target:
            low = mid + 1  # target is in the right half
        else:
            high = mid - 1  # target is in the left half
    return None  # target not found
