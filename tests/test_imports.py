__author__ = ['lorenzo@pramantha.net']


import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
sys.path.append(os.path.dirname("../"))

import unittest


class TestInit(unittest.TestCase):
    """
    This class tests the required packages
    """
    # noinspection PyUnresolvedReferences
    def test_requirements(self):
        print("here")
        try:
            import rdflib
        except ImportError:
            assert False

        try:
            import pyorient
        except ImportError:
            assert False

        try:
            import pymongo
            self.assertEqual(pymongo.version, "2.7.2", "Pymongo version is not GO")
        except ImportError:
            assert False

        try:
            from bson.objectid import ObjectId
        except ImportError:
            assert False

        assert True
