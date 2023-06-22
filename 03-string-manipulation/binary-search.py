def search_binary(arr, val):
    # little optimization
    if val < arr[0] or val > arr[len(arr)-1]:
        return None

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

# item not exists
target = 5
result = search_binary(sorted_list, target)
print(result)  # Output: None

# item less than min value (not exists)
target = 1
result = search_binary(sorted_list, target)
print(result)  # Output: None

# item greater than max value (not exists)
target = 15
result = search_binary(sorted_list, target)
print(result)  # Output: None
