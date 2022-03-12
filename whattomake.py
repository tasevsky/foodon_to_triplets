import rdflib
from rdflib import Graph

g = Graph()
g.load('what_to_make.owl')

# for s in g.__iter__():
#     print(s)

setot = set()

for s in g.subjects():
    setot.add(s)

for s in setot:
    print(s)

#
# for s, o in g.subject_objects(rdflib.term.URIRef('http://www.geneontology.org/formats/oboInOwl#hasExactSynonym')):
#     if not foodOn.get(str(s)):
#         key = str(s)
#         foodOn[key] = str(o)
#

# for s, o in g.subject_objects(rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema')):
#     if not foodOn.get(str(s)):
#         key = str(s)
#         foodOn[key.replace('http://purl.obolibrary.org/obo/', '')] = str(o)
#
#
# for s, o in foodOn.items():
#     print(f"{s}: {o}")

# for s, p, o in g.triples():
#     print(f"{s}: {p}: {o}")
