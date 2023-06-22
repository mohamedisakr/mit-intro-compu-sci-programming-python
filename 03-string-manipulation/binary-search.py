def search_binary(arr, val):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        m = (lo + hi) // 2
        mid = arr[m]
        if mid == val:
            return m
        elif mid < val:
            lo = m + 1
        else:
            hi = m - 1
    return None


# Test the function with some examples
sorted_list = [2, 4, 6, 8, 10, 12, 14]
target = 10
result = search_binary(sorted_list, target)
print(result)  # Output: 4

target = 5
result = search_binary(sorted_list, target)
print(result)  # Output: None
