#!/usr/bin/python3
"""Test for Rectangle class."""

import unittest
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    @classmethod
    def setUpClass(cls):
        """Create objects for testing."""
        cls.obj1 = Rectangle(4, 5, 1, 2, 1)
        cls.obj2 = Rectangle(3, 6, 0, 0, 2)
        cls.obj3 = Rectangle(2, 7, 3, 4, 3)

    @classmethod
    def tearDownClass(cls):
        """Delete objects after testing."""
        del cls.obj1
        del cls.obj2
        del cls.obj3

    def test_init(self):
        """Test Rectangle initialization."""
        self.assertEqual(self.obj1.id, 1)
        self.assertEqual(self.obj1.width, 4)
        self.assertEqual(self.obj1.height, 5)
        self.assertEqual(self.obj1.x, 1)
        self.assertEqual(self.obj1.y, 2)

        self.assertEqual(self.obj2.id, 2)
        self.assertEqual(self.obj2.width, 3)
        self.assertEqual(self.obj2.height, 6)
        self.assertEqual(self.obj2.x, 0)
        self.assertEqual(self.obj2.y, 0)

        self.assertEqual(self.obj3.id, 3)
        self.assertEqual(self.obj3.width, 2)
        self.assertEqual(self.obj3.height, 7)
        self.assertEqual(self.obj3.x, 3)
        self.assertEqual(self.obj3.y, 4)

    def test_area(self):
        """Test area method."""
        self.assertEqual(self.obj1.area(), 20)
        self.assertEqual(self.obj2.area(), 18)
        self.assertEqual(self.obj3.area(), 14)

    def test_display(self):
        """Test display method."""
        self.assertEqual(self.obj1.display(), None)  # Cannot test output directly
        self.assertEqual(self.obj2.display(), None)  # Cannot test output directly
        self.assertEqual(self.obj3.display(), None)  # Cannot test output directly

    def test_str(self):
        """Test __str__ method."""
        self.assertEqual(str(self.obj1), "[Rectangle] (1) 1/2 - 4/5")
        self.assertEqual(str(self.obj2), "[Rectangle] (2) 0/0 - 3/6")
        self.assertEqual(str(self.obj3), "[Rectangle] (3) 3/4 - 2/7")

    def test_update(self):
        """Test update method."""
        self.obj1.update(5, 6, 7, 8, 9)
        self.assertEqual(self.obj1.id, 5)
        self.assertEqual(self.obj1.width, 6)
        self.assertEqual(self.obj1.height, 7)
        self.assertEqual(self.obj1.x, 8)
        self.assertEqual(self.obj1.y, 9)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        expected_dict1 = {'id': 1, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        expected_dict2 = {'id': 2, 'width': 3, 'height': 6, 'x': 0, 'y': 0}
        expected_dict3 = {'id': 3, 'width': 2, 'height': 7, 'x': 3, 'y': 4}
        self.assertEqual(self.obj1.to_dictionary(), expected_dict1)
        self.assertEqual(self.obj2.to_dictionary(), expected_dict2)
        self.assertEqual(self.obj3.to_dictionary(), expected_dict3)


if __name__ == '__main__':
    unittest.main()
