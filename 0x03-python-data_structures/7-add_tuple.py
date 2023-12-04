#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2 = tuple_a[:2]
    b1, b2 = tuple_b[:2]
    if len(tuple_a) < 2:
        a2 = 0
    if len(tuple_b) < 2:
        b2 = 0
    c1 = a1 + b1
    c2 = a2 + b2
    return (c1, c2)
