#!/usr/bin/python3
"""Defines unittests for models/amenity.py.
Unittest class: TestAmenity
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for Amenity class."""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        self.am = Amenity()

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_instance(self):
        self.assertIsInstance(self.am, Amenity)

    def test_id_is_str(self):
        self.assertIsInstance(self.am.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.am.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.am.updated_at, datetime)

    def test_name_attribute(self):
        self.assertTrue(hasattr(self.am, 'name'))
        self.assertIsInstance(self.am.name, str)

    def test_save_updates_updated_at(self):
        initial_updated_at = self.am.updated_at
        sleep(0.05)
        self.am.save()
        self.assertNotEqual(initial_updated_at, self.am.updated_at)

    def test_to_dict_no_extra_keys(self):
        am_dict = self.am.to_dict()
        expected_keys = ['id', '__class__', 'created_at', 'updated_at', 'name']
        self.assertEqual(sorted(am_dict.keys()), sorted(expected_keys))

    def test_init_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        am = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso, name="Example")
        self.assertEqual(am.id, "345")
        self.assertEqual(am.name, "Example")
        self.assertEqual(am.created_at, dt)
        self.assertEqual(am.updated_at, dt)

    def test_save_with_invalid_argument(self):
        with self.assertRaises(TypeError):
            self.am.save("invalid_argument")

    def test_to_dict_with_invalid_argument(self):
        with self.assertRaises(TypeError):
            self.am.to_dict("invalid_argument")


if __name__ == "__main__":
    unittest.main()
