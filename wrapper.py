#
# This Module has the Wrapper class, it contains the connection handler.
# And a set of generic errors
#

__author__ = ['lorenzo@pramantha.net']

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import pyorient


class Wrapper(object):
    """
    This is the class that wraps the connection, Wrapper instance or any of its children has to be called to get connections.
    It creates two clients, one for Mongo one for Orient, each time it get called.
    ----------------------------------------------------------------------

    :method return_mongo: return to other classes and scripts the connection to Mongo
    :method return_orient: return to other classes and scripts the connection to Orient
    """

    __mongo = None   # client
    __orient = None  # client

    __orient_cred = {
        "user": "root",
        "pwd": "su78"
    }

    def __init__(self):
        #
        # Test variable for switching to the test (PMT) or the official database (PTEST)
        #
        self.test = True

        #
        # Initialize Mongo Client
        #
        self.__mongo = MongoClient('localhost', 27017)
        self.__set_mongo_db()

        #
        # Initialize Orient Client
        #
        self.__orient = pyorient.OrientDB("localhost", 2424)
        self.__orient.connect(self.__orient_cred["user"], self.__orient_cred["pwd"])
        self.__set_orient_db()

    def __set_mongo_db(self):
        """create a Mongo client with the right database"""
        if self.test:
            self.__mongo = self.__mongo.PMT
        else:
            self.__mongo = self.__mongo.PTEST

        # print(type(self.__mongod))
        return None

    def __set_orient_db(self):
        """create an Orient client with the right database"""
        try:
            self.__open_orient()
        except pyorient.PyOrientCommandException:
            self.__create_orient()
            self.__open_orient()

        # print(type(self.__orient))
        return None

    def return_mongo(self):
        """returns the connection to the right Mongo database"""
        if self.__mongo is not None:
            return self.__mongo

        raise ConnectionFailure("MongoDB is not up")

    def return_orient(self):
        """returns the connection to the right Orient database"""
        if self.__orient is not None:
            return self.__orient

        raise ConnectionFailure("OrientDB is not up")

    def __open_orient(self):
        """opens a database in the connected __orient client"""
        if self.test:
            db_name = 'PMT'
        else:
            db_name = 'PTEST'

        return self.__orient.db_open(db_name, self.__orient_cred["user"], self.__orient_cred["pwd"])

    def __create_orient(self):
        """create a database in the connected __orient client"""
        if self.test:
            db_name = 'PMT'
        else:
            db_name = 'PTEST'

        return self.__orient.db_create(db_name, pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_PLOCAL)


class DocumentExistNot(Exception):
    """
    Custom exception: trying to fetch a non-existant Document from the Mongo instance
    """
    pass


class DocumentExists(Exception):
    """
    Custom exception: Document already exists in the Mongo instance
    """
    pass


class ValueExistsInList(Exception):
    """
    Custom exception: the script is trying to append to list of values an object that is already in the list
    """
    pass