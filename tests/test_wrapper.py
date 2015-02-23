__author__ = ['lorenzo@pramantha.net']

import unittest
import requests
import simplejson as json
from pprint import pprint

from wrapper import Wrapper


class Test(unittest.TestCase):
    """
    This class collects the tests for the Wrapper() class' instances
    """
    __w = Wrapper()

    def test_dbs_connected(self):
        """tests if both databases are working by printing their clients's strings"""
        print("This is the Mongo client: " + str(self.__w.return_mongo()))
        print("This is the Orient client: " + str(self.__w.return_orient()))

    def test_storage_of_dbpedia_in_both(self):

        #resource ="http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=DESCRIBE+%3Chttp://dbpedia.org/resource/Particle_physics%3E&output=application%2Fld%2Bjson"
        #doc = json.loads(requests.get(resource).text)
        #pprint(doc)
        # client.db_open(db_name, "root", "asdfg")  # open connection

        # CREATE A RECORD
        #record = {'value': doc}
        #cluster_id = client.command("create class DBpedia extends V")
        #rec_position = client.record_create(b'12', record)
        return