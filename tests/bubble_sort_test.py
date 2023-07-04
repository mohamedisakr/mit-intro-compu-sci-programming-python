from unittest import TestCase, main
from searching_sorting.bubble_sort import bubble_sort


class TestBubbleSort(TestCase):

    def test_empty_array(self):
        self.assertEqual(bubble_sort([]), [])

    def test_1_element_array(self):
        arr = [11]
        actual = bubble_sort(arr)
        expected = [11]
        self.assertEqual(actual, expected)

    def test_small_array(self):
        arr = [65, 55, 45, 35, 25, 15, 10]
        actual = bubble_sort(arr)
        expected = [10, 15, 25, 35, 45, 55, 65]
        self.assertEqual(actual, expected)

    def test_sorted_array(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_array_with_duplicates(self):
        self.assertEqual(bubble_sort([3, 2, 1, 3, 2]), [1, 2, 2, 3, 3])

    def test_float_array(self):
        self.assertEqual(bubble_sort([3.14, 2.71, 1.41, 4.20, 0.0]), [
                         0.0, 1.41, 2.71, 3.14, 4.20])

    def test_mixed_array(self):
        arr = [1, "a", 3.14, True, None]
        with self.assertRaises(TypeError):
            bubble_sort(arr)

    def test_large_array(self):
        import random
        arr = [random.randint(0, 100) for _ in range(100)]
        self.assertEqual(bubble_sort(arr), sorted(arr))

    def test_none_input(self):
        with self.assertRaises(TypeError):
            bubble_sort(None)

    def test_single_element(self):
        self.assertEqual(bubble_sort([42]), [42])

    def test_reversed_order(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    main()
