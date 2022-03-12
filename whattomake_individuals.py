import rdflib
from rdflib import Graph

g = Graph()
g.load('what_to_make_ind.owl')

triplets = []
for s in g.__iter__():
    subject = s[0]
    predcate = s[1]
    object = s[2]
    triplets.append([subject, predcate, object])

#print(triplets)

for i in range(0, len(triplets)):
    if "FOODON_" in str(triplets[i][2]).split("/")[-1].split('#')[-1]:
        continue
    triplets[i][2] = str(triplets[i][2]).split("/")[-1].split('#')[-1]
    triplets[i][0] = str(triplets[i][0]).split("/")[-1]
    triplets[i][1] = str(triplets[i][1]).split("/")[-1].split("#")[-1]

print(triplets[0:10])

