#!/usr/bin/python3
"""test of file_storage"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class FileStorageTest(unittest.TestCase):
    """test"""

    def test_file_path(self):
        fs = FileStorage()
        a = fs._FileStorage__file_path
        self.assertEqual(a, "file.json")

    def test_everything(self):
        fs = FileStorage()
        fs.all()
        fs.reload()
        self.assertFalse(len(fs.all()) == 0)
