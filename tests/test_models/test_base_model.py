#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import os
import models
import unittest
from datetime import datetime, timedelta
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for BaseModel class."""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        self.bm = BaseModel()

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
        self.assertIsInstance(self.bm, BaseModel)

    def test_id_is_str(self):
        self.assertIsInstance(self.bm.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.bm.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_save_updates_updated_at(self):
        initial_updated_at = self.bm.updated_at
        sleep(0.05)
        self.bm.save()
        self.assertNotEqual(initial_updated_at, self.bm.updated_at)

    def test_to_dict_contains_correct_keys(self):
        bm_dict = self.bm.to_dict()
        expected_keys = ['id', '__class__', 'created_at', 'updated_at']
        self.assertEqual(sorted(bm_dict.keys()), sorted(expected_keys))

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    def test_instantiation_with_valid_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_invalid_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)


if __name__ == "__main__":
    unittest.main()
