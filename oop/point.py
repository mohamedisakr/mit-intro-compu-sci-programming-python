"""
Represents a point in a coordinate plane.
"""


class Point:
    """A class that represents a point in a coordinate plane."""

    def __init__(self, x, y):
        """Initialize the point with x and y coordinates.

        Args:
            x (float): The x coordinate of the point.
            y (float): The y coordinate of the point.

        Raises:
            TypeError: If x or y is not an int or a float.
        """
        # check if x and y are of type int or float
        if not isinstance(x, (int, float)):
            raise TypeError(f"x must be an int or a float, not {type(x)}")

        if not isinstance(y, (int, float)):
            raise TypeError(f"y must be an int or a float, not {type(y)}")

        self.x = x
        self.y = y

    def distance(self, p):
        """
        Return euclidian distance between 2 coordinate points.

        Args:
            point_1 (Point): The first point.
            point_2 (Point): The second point.

        Raises:
            TypeError: If x or y is not an int or a float.
        """
        if not isinstance(self, Point):
            raise TypeError(
                f"first argument must be a Point, not {type(self)}")

        if not isinstance(p, Point):
            raise TypeError(f"second argument must be a Point, not {type(p)}")

        diff_x_sq = (self.x - p.x)**2
        diff_y_sq = (self.y - p.y)**2
        return (diff_x_sq + diff_y_sq)**0.5

    def __repr__(self):
        """Return a string representation of the point.

        Returns:
            str: A string in the form of "Point(x, y)".
        """
        return f"Point({self.x}, {self.y})"
