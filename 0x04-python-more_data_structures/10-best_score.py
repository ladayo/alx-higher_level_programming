#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        k = list(a_dictionary.keys())
        v = list(a_dictionary.values())
        return (k[v.index(max(v))])
    else:
        return None
