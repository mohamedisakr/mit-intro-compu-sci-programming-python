def bubble_sort(arr):
    if len(arr) == 0:
        return []

    if all(not isinstance(item, (int, float, str)) for item in arr):
        raise TypeError(
            f"item must be an int, float or str")  # , not {type(item)}

    if len(arr) == 0:
        return []

    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


'''
def bubble_sort(list):
    unsorted_until_index = len(list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
        unsorted_until_index -= 1
    return list
'''

'''
def bubble_sort(arr):
    """ my implementation (naive)
    """
    for i, elem in enumerate(arr):
        for j, el in enumerate(arr):
            if (arr[i] < arr[j]):
                arr[i], arr[j] = arr[j], arr[i]

    return arr
'''

'''
arr = [5, 1, 4, 2, 8]
sorted_arr = bubble_sort(arr)
print(f'sorted array: {sorted_arr}')
print(sorted_arr == [1, 2, 4, 5, 8])
'''
