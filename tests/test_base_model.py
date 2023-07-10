#!/usr/bin/python3
"""BaseModel"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """This class contains test methods to test the
    behavior of the BaseModel class."""

    def test_create_object(self):
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)

    def test_check_id(self):
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_check_created_at(self):
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)

    def test_check_updated_at(self):
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime)

    def test_save(self):
        bm = BaseModel()
        hs = bm.updated_at
        bm.save()
        new_hs = bm.updated_at
        self.assertNotEqual(hs, new_hs)

    def test_to_dict(self):
        bm = BaseModel()
        dict_result = bm.to_dict()
        self.assertIsInstance(dict_result, dict)
        self.assertIn("__class__", dict_result)
        self.assertEqual(dict_result["__class__"], "BaseModel")
        self.assertIn("updated_at", dict_result)
