__author__ = ['lorenzo@pramantha.net']

import unittest
import pyorient
from pprint import pprint

from wrapper import Wrapper


class Test(unittest.TestCase):
    """
    This class tests the functionality of Orient
    """
    __w = Wrapper()
    __client = __w.return_orient()

    def test_orient_db_exists(self):
        """tests if the database initialized by Wrapper() holds the test db (PMT)"""
        exist = self.__client.db_exists('PMT', pyorient.STORAGE_TYPE_PLOCAL)
        if exist:
            print(exist)
            assert True
        else:
            print(exist)
            assert False


    #print(rec_position)
    # CREATE A CLASS
    #client.command("create class Animal extends V")

    # Insert a new value
    #client.command("insert into Animal set name = 'rat', specie = 'rodent'")

    # DROP DB
    # client.db_drop(db_name)









