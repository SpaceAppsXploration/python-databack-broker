__author__ = 'lorenzo'


import unittest
from pprint import pprint
import simplejson as json
import html.parser

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
    """
    Set of tests for Concepts API
    """
    def test_endpoints_http(self):
        """
        HTTPConnection:
        https://docs.python.org/3/library/http.client.html
        """
        url = "127.0.0.1:8080"
        api = ["/concepts/"]

        import http.client
        from urllib.parse import quote
        import codecs

        for a in api:
            conn = http.client.HTTPConnection(url)
            conn.request("GET", a)
            response = conn.getresponse()
            print(response.status, response.reason)
            content = response.read().decode()
            conn.close()
            print(type(content))
            if response.status == 200:
                #pprint(content)
                for i, e in enumerate(json.loads(content)):
                    to_test = quote(a + e["skos:prefLabel"])
                    conn = http.client.HTTPConnection(url)
                    conn.request("GET", to_test)
                    r = conn.getresponse()
                    if r.status == 200:
                        #pprint(str(i) + to_test + " >> " + str(r.status_code))
                        pass
                    else:
                        print('Keys Error ' + str(r.status) + ' : ' + to_test)
                        #print('\n ' + str(r.msg))
                    conn.close()
            else:
                conn.close()
                raise ConnectionError(response.status, response.reason)



