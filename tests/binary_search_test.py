from unittest import TestCase, main
from program_efficiency.binary_search import binary_search


class TestBinarySearch(TestCase):

    def test_empty_array(self):
        # test case: empty array
        self.assertEqual(binary_search([], 5), None)

    def test_lower_bound_below_min(self):
        # test case: target is less than min value
        arr = [2, 4, 6, 8, 10]
        self.assertEqual(binary_search(arr, 1), None)

    def test_upper_bound_above_max(self):
        # test case: target is greater than max value
        arr = [2, 4, 6, 8, 10]
        self.assertEqual(binary_search(arr, 11), None)

    def test_single_element_array(self):
        # test case: single element array
        self.assertEqual(binary_search([5], 5), 0)
        self.assertEqual(binary_search([5], 6), None)

    def test_multiple_element_array(self):
        # test case: multiple element array
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(arr, 1), 0)
        self.assertEqual(binary_search(arr, 9), 4)
        self.assertEqual(binary_search(arr, 5), 2)

    def test_array_with_non_exist_target(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(arr, 4), None)
        self.assertEqual(binary_search(arr, -1), None)
        self.assertEqual(binary_search(arr, 10), None)

    def test_array_with_duplicate_elements(self):
        """ test case: array with duplicate elements"""
        arr = [1, 2, 2, 3, 4, 4, 5]
        self.assertEqual(binary_search(arr, 2), 1)
        self.assertEqual(binary_search(arr, 6), None)
        # self.assertEqual(binary_search(arr, 4), 4)

    def test_array_with_negative_elements(self):
        """ array with negative elements"""
        arr = [-5, -3, -1, 0, 2, 4]
        self.assertEqual(binary_search(arr, -3), 1)
        self.assertEqual(binary_search(arr, 0), 3)
        self.assertEqual(binary_search(arr, -6), None)

    def test_array_with_mixed_types_of_elements(self):
        """ array with mixed types of elements"""
        arr = [1, "a", True, None, 3.14]
        self.assertRaises(TypeError, binary_search, arr, "a")
        # self.assertRaises(TypeError, binary_search, arr, True)
        # self.assertRaises(TypeError, binary_search, arr, None)

    # def test_array_with_mixed_types_of_elements_2(self):
    #     """ array with mixed types of elements"""
    #     arr = [1, "a", True, None, 3.14]
    #     with self.assertRaises(TypeError):
    #         binary_search(arr, True)
    #     # self.assertRaises(TypeError, binary_search, arr, True)

    def test_array_with_mixed_types_of_elements_3(self):
        """ array with mixed types of elements"""
        arr = [1, "a", True, None, 3.14]
        self.assertRaises(TypeError, binary_search, arr, None)

    def test_invalid_input(self):
        # test case: invalid input
        self.assertRaises(TypeError, binary_search, None, 5)
        self.assertRaises(TypeError, binary_search, "hello", "e")

    def test_odd(self):
        arr = [0, 2, 4, 6, 8, 10, 12, 14, 16]
        target = 9
        self.assertEqual(binary_search(arr, target), None)

    def test_duplicate_odd(self):
        arr = [0, 2, 4, 6, 6, 8, 10, 12, 14, 16, 18]
        target = 6
        self.assertEqual(binary_search(arr, target), 3)

    def test_duplicate_even(self):
        arr = [0, 2, 4, 6, 6, 8, 10, 12, 14, 16]
        target = 6
        self.assertEqual(binary_search(arr, target), 4)


'''
https://www.digizol.com/2013/08/java-binary-search-recursive-testcases.html
SortedEvenArray
AsFirstInSortedArray
AtEndInSortedArray
InMiddleInSortedArray
AnywhereInSortedArray
SortedArray
'''

if __name__ == '__main__':
    main()
