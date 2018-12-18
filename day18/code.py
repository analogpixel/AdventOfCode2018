#!/usr/bin/env python

import copy
input_file = "input.txt"

def adj(mapData, x,y):
    ret = []
    for xx in range(x-1, x+2):
        for yy in range(y-1, y+2):
            
            if xx >= 0 and xx < len(mapData[0]):
                if yy >= 0 and yy < len(mapData):
                    if not (xx==x and yy==y):
                        ret.append(mapData[yy][xx])
    return ret

def countThings(x,y,mapData):
    t = 0
    l = 0
    o = 0
    for a in adj(mapData, x,y):
        if a == '#':
            l += 1
        elif a == '.':
            o += 1
        elif a == '|':
            t += 1
    return (t,l,o)

def printMap(mapData):
    for l in mapData:
        print( "".join(l) )
    print("")
input = list(map( lambda x: x.strip(), open(input_file).readlines() ))
mapData = []
for line in input:
    mapData.append( list(line) )

printMap(mapData)

last = 0
for m in range(0,1000000000):
    newData = copy.deepcopy(mapData)
    for x in range(0, len(mapData[0])):
        for y in range(0, len(mapData)):
            (t,l,o) = countThings(x,y, mapData)
            
            if mapData[y][x] == '.' and t >= 3:
                newData[y][x] = '|'

            
            if mapData[y][x] == '|' and l >= 3:
                newData[y][x] = '#'
            
            if mapData[y][x] == '#' and l >= 1 and t >=1:
                newData[y][x] = '#'
            
            if mapData[y][x] == '#' and not (l >=1 and t >=1):
                newData[y][x] = '.'
                
    if m % 1000 == 0:
        #print(1000000000 - m)
        t = 0
        l = 0
        o = 0
        for i in mapData:
            for j in i:
                if j == '#':
                    l +=1
                elif j == '.':
                    o += 1
                elif j == '|':
                    t +=1
        print("tree:{} lumberyard:{} openspace:{} :: {} ".format(t,l,o,m))
        #zoo = t * l 
        #print(zoo, zoo - last)
        #print()
        #last = zoo

    mapData = copy.deepcopy(newData)

printMap(newData)

t = 0
l = 0
o = 0
for i in mapData:
    for j in i:
        if j == '#':
            l +=1
        elif j == '.':
            o += 1
        elif j == '|':
            t +=1

print("tree:{} lumberyard:{} openspace:{}".format(t,l,o))

print(t*l)