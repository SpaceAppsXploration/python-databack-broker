__author__ = 'lorenzo@pramantha.net'


from aylienapiclient import textapi
from pprint import pprint

c = textapi.Client("667ed32e", "a177807738ffcb901890be0ce7103ae9")

txt = """Venus is a dim world of intense heat and volcanic activity. Similar in structure
                and size to Earth, Venus\' thick, toxic atmosphere traps heat in a runaway \'greenhouse effect.\' The scorched
                world has temperatures hot enough to melt lead. Glimpses below the clouds reveal volcanoes and deformed mountains.
                Venus spins slowly in the opposite direction of most planets."""

s = c.Hashtags({'text': txt})
e = c.Entities({'text': txt})
g = c.Concepts({'text': txt})
h = c.Classify({'text': txt})
j = c.Extract({'url': "http://en.wikipedia.org/wiki/Venus", "best_image": True})
u = c.UnsupervisedClassify({'text': txt, 'class': ['astronomy', 'geology', 'mythology', 'atmosphere', 'exploration']})  # needs min two and max five classes

pprint(s)
pprint(e)
pprint(g)
pprint(h)
pprint(j)
pprint(u)

