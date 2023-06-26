from unittest import TestCase, main
from oop.point import Point


class TestPoint(TestCase):
    """A class that tests the Point class."""

    def test_init(self):
        """Test the __init__ method of the Point class."""
        # create a point with x=1 and y=2
        p = Point(1, 2)
        # check if the x and y attributes are set correctly
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_init_int(self):
        # try to create a point with int coordinate x=1 and y=5
        p = Point(1, 5)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 5)

    def test_init_float(self):
        # try to create a point with int coordinate x=1.5 and y=5.25
        p = Point(1.5, 5.25)
        self.assertEqual(p.x, 1.5)
        self.assertEqual(p.y, 5.25)

    def test_init_type_error_string(self):
        """Test the __init__ method of the Point class for type errors."""
        # try to create a point with x="a" and y=5
        with self.assertRaises(TypeError):
            p = Point("a", 5)

    def test_init_type_error_array(self):
        """Test the __init__ method of the Point class for type errors."""
        # try to create a point with x=6 and y=[7]
        with self.assertRaises(TypeError):
            p = Point(6, [7])

    def test_distance(self):
        """Test the distance method with valid Point arguments."""
        # create two points with x=1, y=2 and x=4, y=6
        p1 = Point(1, 2)
        p2 = Point(4, 6)
        # call the distance method with the two points
        result = p1.distance(p2)
        # check if the result is as expected (5.0)
        self.assertEqual(result, 5.0)

    def test_distance_same_point(self):
        """Test the distance method with the same Point argument."""
        # create a point with x=3 and y=4
        p = Point(3, 4)
        # call the distance method with the same point
        result = p.distance(p)
        # check if the result is as expected (0.0)
        self.assertEqual(result, 0.0)

    def test_distance_type_error_string(self):
        """Test the distance method for type errors."""
        # create a point with x=1 and y=2
        p = Point(1, 2)

        # try to call the distance method with an invalid argument
        with self.assertRaises(TypeError):
            result = p.distance("a")

    def test_distance_type_error_array(self):
        """Test the distance method for type errors."""
        # create a point with x=1 and y=2
        p = Point(3, 4)

        # try to call the distance method with another invalid argument
        with self.assertRaises(TypeError):
            result = p.distance([3, 4])

    def test_repr(self):
        """Test the __repr__ method with a valid Point object."""
        # create a point with x=1 and y=2
        p = Point(1, 2)
        # call the __repr__ method on the point
        result = repr(p)
        # check if the result is as expected ("Point(1, 2)")
        self.assertEqual(result, "Point(1, 2)")

    def test_repr_negative(self):
        """Test the __repr__ method with a Point object with negative coordinates."""
        # create a point with x=-3 and y=-4
        p = Point(-3, -4)
        # call the __repr__ method on the point
        result = repr(p)
        # check if the result is as expected ("Point(-3, -4)")
        self.assertEqual(result, "Point(-3, -4)")

    def test_repr_zero(self):
        """Test the __repr__ method with a Point object with zero coordinates."""
        # create a point with x=0 and y=0
        p = Point(0, 0)
        # call the __repr__ method on the point
        result = repr(p)
        # check if the result is as expected ("Point(0, 0)")
        self.assertEqual(result, "Point(0, 0)")


if __name__ == '__main__':
    main()
