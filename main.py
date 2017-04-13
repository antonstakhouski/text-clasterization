#!/usr/bin/env python
#  import re


def gloss_open(name):
    tfile = open("glossary/" + name, "r")
    dct = {a: 0 for a in tfile.read().lower().split("\n")}
    tfile.close()
    return dct


discps = ("econ", "phyl", "med")

glossaries = list()
for dcp in discps:
    glossaries.append((gloss_open(dcp), dcp))
vec = {a: 0 for a in discps}

#  print(glossaries[0][0])

#  for gloss in glossaries:
#      for term in gloss[0]:
#          vec[gloss[1]] += len([m.start() for m in re.finditer(term, txt)])

for discp in discps:
    print(discp)
    for num in range(1, 6):
        text = open("txt/" + discp + "/" + str(num), "r")
        txt = text.read().lower().split("\n")
        for line in txt:
            for word in line.split():
                #  print(word)
                for gloss in glossaries:
                    if word in gloss[0]:
                        vec[gloss[1]] += 1
        text.close()
        print(num, vec)
