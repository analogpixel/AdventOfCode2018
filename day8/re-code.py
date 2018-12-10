#!/usr/bin/env python

input_file = "test_input.txt"

input = open(input_file).readlines()[0].strip().split(' ')


def parseData(d,i):

    if len(d) == 0:
        return

    child_nodes = int(d[0])
    meta_nodes = int(d[1])
    
    if child_nodes == 0:
        print("Meta nodes ", i ,  ":", d[2:2+meta_nodes])
        return d[2+meta_nodes:]

    else:
        for c in range(0, child_nodes):
            d = parseData(d[2:], i+1+c)

        print("Meta nodes ", i ,  d[0:meta_nodes])
        return d[meta_nodes:]


parseData(input,0)
