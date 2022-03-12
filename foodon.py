import rdflib
from rdflib import Graph

foodOn = {}

g = Graph()
g.load('food_riste.owl')
#g.load('http://purl.obolibrary.org/obo/foodon/releases/2020-09-14/foodon.owl')
g.load('http://purl.obolibrary.org/obo/bfo/2.0/bfo.owl')
g.load('http://purl.obolibrary.org/obo/foodon/imports/chebi_import.owl')
#g.load('http://purl.obolibrary.org/obo/foodon/imports/ecocore_import.owl')
g.load('http://purl.obolibrary.org/obo/foodon/imports/envo_import.owl')
g.load('http://purl.obolibrary.org/obo/foodon/imports/foodon_product_import.owl')
g.load('http://purl.obolibrary.org/obo/foodon/imports/gaz_import.owl')
g.load('http://purl.obolibrary.org/obo/foodon/imports/geem_import.owl')
#g.load('http://purl.obolibrary.org/obo/foodon/imports/hancestro_import.owl')
g.load('http://purl.obolibrary.org/obo/foodon/imports/langual_deprecated_import.owl')
g.load('http://purl.obolibrary.org/obo/foodon/imports/metadata_import.owl')
g.load('http://purl.obolibrary.org/obo/foodon/imports/ncbitaxon_import.owl')
#g.load('http://purl.obolibrary.org/obo/foodon/imports/ncit_import.owl')
#g.load('http://purl.obolibrary.org/obo/foodon/imports/obi_import.owl')
#g.load('http://purl.obolibrary.org/obo/foodon/imports/pato_import.owl')
#g.load('http://purl.obolibrary.org/obo/foodon/imports/peco_import.owl')
# g.load('http://purl.obolibrary.org/obo/foodon/imports/po_import.owl')
# g.load('http://purl.obolibrary.org/obo/foodon/imports/product_type_import.owl')
# g.load('http://purl.obolibrary.org/obo/foodon/imports/ro_import.owl')
# g.load('http://purl.obolibrary.org/obo/foodon/imports/robot_pasta.owl')
# g.load('http://purl.obolibrary.org/obo/foodon/imports/robot_wine.owl')
# g.load('http://purl.obolibrary.org/obo/foodon/imports/uberon_import.owl')
# g.load('http://purl.obolibrary.org/obo/foodon/imports/uo_import.owl')


# for s in g.__iter__():
#     print(s)

setot = set()

for s in g.predicates():
    setot.add(s)

for s in setot:
    print(s)

#
# for s, o in g.subject_objects(rdflib.term.URIRef('http://www.geneontology.org/formats/oboInOwl#hasExactSynonym')):
#     if not foodOn.get(str(s)):
#         key = str(s)
#         foodOn[key] = str(o)
#

for s, o in foodOn.items():
    print(f"{s}: {o}")

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
