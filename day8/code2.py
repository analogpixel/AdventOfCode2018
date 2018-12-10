#!/usr/bin/env python

input_file = "input.txt"

input = open(input_file).readlines()[0].strip().split(' ')

total = 0

def parseData(d,i):
    debug = False

    if len(d) == 0:
        return ([],0)

    child_nodes = int(d[0])
    meta_nodes = int(d[1])
    
    if child_nodes == 0:
        print("Meta nodes ", chr(65 + i) ,  ":", d[2:2+meta_nodes])
        return (d[2+meta_nodes:], sum(map(int, d[2:2+meta_nodes])))

    else:
        
        d = d[2:]
        tots = []
        for c in range(0, child_nodes):
            (d,tot) = parseData(d, i+1+c)
            tots.append(tot) # add this total to the array
    
        print(tots)
        total = 0
        for z in d[0:meta_nodes]:
            print("meta node:", z)
            if (int(z)-1) < len(tots):
                total += tots[int(z)-1]
        
        print("total:", total)
        
        return (d[meta_nodes:], total)

print ( parseData(input,0) )
