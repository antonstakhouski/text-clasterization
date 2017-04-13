#!/usr/bin/env python
import os


def gloss_open(name):
    tfile = open("glossary/" + name, "r")
    dct = {a: 0 for a in tfile.read().lower().split("\n")}
    tfile.close()
    return dct


def gloss_init(glossaries):
    for dcp in discps:
        glossaries.append([gloss_open(dcp), dcp])
    return glossaries


def clear_glossies(glossaries):
    for gloss in glossaries:
        gloss[0] = {a: 0 for a in gloss[0]}
    return glossaries


def slice_find(string, substring):
    pos = string.find(substring)
    if pos >= 0:
        return string[:pos]
    else:
        return string


def print_gloss(glossaries):
    for gloss in glossaries:
        print("-----" + gloss[1] + "------")
        for el in gloss[0]:
            if gloss[0][el] > 0:
                print(el)


def count_terms(text, glossaries, vec):
    term_sum = 0
    for line in text:
        word = line
        word = slice_find(word, "|")
        word = slice_find(word, "?")
        for gloss in glossaries:
            if word in gloss[0]:
                term_sum += 1
                gloss[0][word] += 1
                vec[gloss[1]] += 1
    return term_sum


def get_vectors(discps, glossaries):
    vecs = list()
    for discp in discps:
        print(discp)
        for num in range(1, 6):
            vec = {a: 0 for a in discps}
            glossaries = clear_glossies(glossaries)
            path = "txt/" + discp + "/" + str(num)
            lemmas = os.popen("./mystem -ln " + path).read().lower().split()
            res = count_terms(lemmas, glossaries, vec)
            term_sum = res
            #  print_gloss(glossaries)
            for gloss in glossaries:
                vec[gloss[1]] = vec[gloss[1]] / term_sum
            vecs.append([discp, num, vec])
            print(num, vec)
    return vecs


discps = ("econ", "phyl", "med")

glossaries = list()
glossaries = gloss_init(glossaries)

vecs = list()
vecs = get_vectors(discps, glossaries)
