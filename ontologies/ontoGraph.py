__author__ = 'lorenzo'

from pprint import pprint

import simplejson as json
from rdflib import Graph

from ontologies.contexts import ASTRONOMY_FLATTENED, ASTRONOMY_N3, SOLARSYSTEM_N3


jsonld = json.dumps(ASTRONOMY_FLATTENED)

#pprint(jsonld)

g = Graph().parse(data=SOLARSYSTEM_N3, format='n3')

for stmt in g:
    pprint(stmt)

