#!/usr/bin/env python

from functools import reduce
import math

input_file = "input.txt"
consta = list(map( lambda x: list(map(int, x.strip().split(','))), open(input_file).readlines() ))

def getList(data,indexes, currentList):
    for i in indexes:
        if not i in currentList:
            currentList += getList(data,data[i], currentList + [i] )
    
    return set(currentList)


def dist(p1, p2):
    return (sum(map(lambda x,y: abs(x-y), p1,p2)) )

neigh = [] 

for i in consta:
    close = []
    count = 0
    for j in consta:
        if dist(i,j) <= 3:
            close.append(count)
        count += 1

    neigh.append(close)


for i in range(0, len(neigh)):
    for z in getList(neigh, neigh[i], [] ):
        if not z == i:
            neigh[z] = []

count = 0
for n in neigh:
    if len(n) > 0:
        count +=1
        print(n)

print(count)



"""
buckets = [ [list(map(int, input[0].split(',')))] ]

for l in input[1:]:
    p1 = list(map(int, l.split(',')))

    m = False
    for b in buckets:
        print(  list(map(lambda x:  dist(p1, x) , b)))
        
        if any(map(lambda x:  dist(p1, x) <=3, b)):
            b.append(p1)
            
            m=True

        
print(len(buckets))

for b in buckets:
    print(b)

"""
