__author__ = 'lorenzo'

from pprint import pprint

import simplejson as json
from rdflib import Graph

# >>> from rdflib.graph import Graph
# >>> g = Graph()
# >>> g.parse("demo.nt", format="nt")

def load_sensors_graph():
    """
    Load the N-TRIPLES into a RDFLib graph
    :return: a reflib.Graph
    """
    from ontologies.data.sensors_n3 import SENSORS_N3
    g = Graph().parse(data=SENSORS_N3, format='n3')
    return g

#
# Load the sensors graph and print the first random statement as example
#
g = load_sensors_graph()
for stmt in g:
    pprint(stmt)
    break

print('--------------------------------------------------------------------------------')

def get_object_type_from_graph(type_uri):
    """
    Return a list of subjects that have some given property
    :param type_uri: URI of a predicate
    :return: a list
    """
    from rdflib import URIRef
    from rdflib.namespace import RDF

    # Filter URIs that are properties
    property = URIRef(type_uri)
    results = []
    for s,p,o in g.triples( (None, RDF.type, property ) ):
        results.append(s)
    return results


#
# Find subjects for a given property
#
properties = get_object_type_from_graph('http://www.w3.org/2002/07/owl#ObjectProperty')
pprint(properties)
print('--------------------------------------------------------------------------------')

from rdflib import Namespace
from rdflib.namespace import OWL
# Querying with SPARQL

# >>> n = Namespace("http://www.w3.org/2002/07/owl#")
# >>> print(n.ObjectProperty) # as attribute

#
# Run a SPARQL query on the graph
#

q1 = g.query('SELECT * WHERE { ?p a owl:ObjectProperty }', initNs={ 'owl': OWL })
for row in q1:
    print(row)


