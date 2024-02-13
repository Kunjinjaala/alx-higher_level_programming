#!/usr/bin/python3
"""Test for Base class."""

import unittest
import os
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    @classmethod
    def setUpClass(cls):
        """Create objects for testing."""
        cls.obj1 = Base(1)
        cls.obj2 = Base(2)
        cls.obj3 = Base(3)

    @classmethod
    def tearDownClass(cls):
        """Delete objects after testing."""
        del cls.obj1
        del cls.obj2
        del cls.obj3

    def test_init(self):
        """Test Base initialization."""
        self.assertEqual(self.obj1.id, 1)
        self.assertEqual(self.obj2.id, 2)
        self.assertEqual(self.obj3.id, 3)

    def test_to_json_string(self):
        """Test to_json_string method."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 1, 'name': 'John'}]),
                         '[{"id": 1, "name": "John"}]')

    def test_save_to_file(self):
        """Test save_to_file method."""
        obj_list = [self.obj1, self.obj2, self.obj3]
        Base.save_to_file(obj_list)
        self.assertTrue(os.path.exists("Base.json"))

    def test_from_json_string(self):
        """Test from_json_string method."""
        self.assertEqual(Base.from_json_string(None), "[]")
        self.assertEqual(Base.from_json_string("[]"), [])
        json_string = '[{"id": 1, "name": "John"}]'
        self.assertEqual(Base.from_json_string(json_string),
                         [{'id': 1, 'name': 'John'}])

    def test_create(self):
        """Test create method."""
        dummy_dict = {'id': 4, 'name': 'Jane'}
        dummy = Base.create(**dummy_dict)
        self.assertEqual(dummy.id, 4)
        self.assertEqual(dummy.name, 'Jane')

    def test_load_from_file(self):
        """Test load_from_file method."""
        obj_list = Base.load_from_file()
        self.assertEqual(len(obj_list), 3)
        self.assertEqual(obj_list[0].id, 1)
        self.assertEqual(obj_list[1].id, 2)
        self.assertEqual(obj_list[2].id, 3)


if __name__ == '__main__':
    unittest.main()
