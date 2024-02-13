#!/usr/bin/python3
"""Test for Square class."""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_init(self):
        """Test Square initialization."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, None)

        s2 = Square(10, 2, 3, 4)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 4)

    def test_str(self):
        """Test Square __str__ method."""
        s1 = Square(5, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (4) 2/3 - 5")

    def test_size_property(self):
        """Test size property."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)

    def test_update(self):
        """Test update method."""
        s1 = Square(5, 2, 3, 4)
        s1.update(10, 3, 4, 5)
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 5)

        s2 = Square(5, 2, 3, 4)
        s2.update(size=10, x=3, y=4, id=10)
        self.assertEqual(s2.id, 10)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 4)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s1 = Square(5, 2, 3, 4)
        s1_dict = s1.to_dictionary()
        expected_dict = {'id': 4, 'size': 5, 'x': 2, 'y': 3}
        self.assertDictEqual(s1_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
