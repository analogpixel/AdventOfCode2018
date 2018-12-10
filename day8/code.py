#!/usr/bin/env python

input_file = "input.txt"

input = open(input_file).readlines()[0].strip().split(' ')

total = 0

def parseData(d,i):
    debug = False
    global total

    if len(d) == 0:
        return

    child_nodes = int(d[0])
    meta_nodes = int(d[1])
    
    if child_nodes == 0:
        if debug: print(chr(65+i), " has no child nodes current stack:", d) 
        print("Meta nodes ", chr(65 + i) ,  ":", d[2:2+meta_nodes])
        total += sum(map(int, d[2:2+meta_nodes]))
        if debug: print("returning:", d[2+meta_nodes:] )
        return d[2+meta_nodes:]

    else:
        if debug: print(chr(65 + i) , "has ", child_nodes , " child nodes current stack:", d)
        d = d[2:]
        for c in range(0, child_nodes):
            if debug: print("search child node:", chr(65 + c+1), " with stack:", d)
            d = parseData(d, i+1+c)
        print("Meta nodes ", chr(65 + i) ,  d[0:meta_nodes])
        total += sum( map(int, d[0:meta_nodes] ))
        if debug: print("returning:", d[meta_nodes:])
        return d[meta_nodes:]

parseData(input,0)

print(total)