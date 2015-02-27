__author__ = 'lorenzo'


import unittest
from pprint import pprint
import simplejson as json

from tools import retrieve_json, retrieve_url, raise404


class TestConceptsAPI(unittest.TestCase):

    def test_request_subjects(self):

        url = "http://127.0.0.1:8080/concepts/subjects"

        try:
            response = retrieve_json(url)
        except Exception as e:
            raise e

        print("count: " + str(len(response)))

        for s in response:
            print(s["chronos:code"])
            print(s["skos:prefLabel"])
            print(s["chronos:group"])
            print("\n")


class TestConceptsAPI(unittest.TestCase):
    def test_endpoints(self):
        url = "http://127.0.0.1:8080/"
        api = ["concepts/"]

        def ask(endpnt):
            try:
                res = retrieve_url(endpnt)
            except Exception as e:
                raise e
            return res

        for a in api:
            response = ask(url + a)
            if response.status_code == 200:
                for i, e in enumerate(json.loads(response.text)):
                    #print(i, e)
                    to_test = url + a + e["skos:prefLabel"]
                    r = ask(to_test)
                    if r.status_code == 200:
                        #pprint(str(i) + to_test + " >> " + str(r.status_code))
                        pass
                    elif r.status_code == 404:
                        print('Keys Error 404: ' + to_test)
                    else:
                        print('Keys Error ' + r.status_code + ' : ' + to_test)
            else:
                raise raise404


"""
Response Object:
     __attrs__ = [
        '_content',
        'status_code',
        'headers',
        'url',
        'history',
        'encoding',
        'reason',
        'cookies',
        'elapsed',
        'request',
    ]
"""