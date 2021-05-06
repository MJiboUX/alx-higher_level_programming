#!/usr/bin/python3
Prototype: def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for i in new.keys():
        new[i] *= 2
    return (new)
