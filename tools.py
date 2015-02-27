__author__ = 'lorenzo'


import requests
import simplejson as json
import html.parser
from codecs import raw_unicode_escape_decode


def retrieve_url(url):
    """
    Utility: URL's response fetching
    :param url:
    :return:
    """
    return requests.get(url)


def retrieve_json(url, method='GET', data=None):
    """
    Utility: URL's body fetching
    :rtype : dict()
    :param url: URL to fetch
    :param method: the method to use for the request
    :param data: if method is POST, pass also some data for request's body
    :return: dictionary from the response's body
    """
    print(url)
    if method == 'GET':
        try:   # avoid unicode escaping problems (double backslash encoding)
            h = html.parser.HTMLParser()
            text = h.unescape(requests.get(url).text)
            return json.loads(raw_unicode_escape_decode(text)[0])
        except json.JSONDecodeError as e:
            raise e
    elif method == 'POST':
        if data is not None:
            try:
                h = html.parser.HTMLParser()
                text = h.unescape(requests.post(url, data=data).text)
                return json.loads(raw_unicode_escape_decode(text)[0])  # using bs4 to treat html entities
            except json.JSONDecodeError as e:
                return e
        else:
            raise Exception('retrieve_json(): data for POST cannot be None')
    else:
        raise Exception('retrieve_json(): Wrong Method')


raise404 = requests.HTTPError