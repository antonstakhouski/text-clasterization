#!/usr/bin/env python
import os
#  import re


def gloss_open(name):
    tfile = open("glossary/" + name, "r")
    dct = {a: 0 for a in tfile.read().lower().split("\n")}
    tfile.close()
    return dct


discps = ("econ", "phyl", "med")

glossaries = list()
for dcp in discps:
    glossaries.append([gloss_open(dcp), dcp])
#  print(glossaries[0][0])

#  for gloss in glossaries:
#      for term in gloss[0]:
#          vec[gloss[1]] += len([m.start() for m in re.finditer(term, txt)])

for discp in discps:
    print(discp)
    for num in range(1, 6):
        vec = {a: 0 for a in discps}
        for gloss in glossaries:
            gloss[0] = {a: 0 for a in gloss[0]}
        path = "txt/" + discp + "/" + str(num)
        res = os.popen("./mystem -ln " + path).read()
        res = res.lower().split()
        #  print(res)
        for line in res:
            word = line
            pos = word.find("|")
            if pos >= 0:
                word = word[:pos]
            pos = word.find("?")
            if pos >= 0:
                word = word[:pos]
            #  print(word)
            for word in line.split():
                #  print(word)
                for gloss in glossaries:
                    if word in gloss[0]:
                        gloss[0][word] += 1
                        vec[gloss[1]] += 1
        #  for gloss in glossaries:
        #      print("-----" + gloss[1] + "------")
        #      for el in gloss[0]:
        #          #  print(gloss[0])
        #          if gloss[0][el] > 0:
        #              print(el)
        print(num, vec)
