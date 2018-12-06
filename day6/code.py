#!/usr/bin/env python

import numpy as np


def dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

input = list(map( lambda x: x.strip(), open("input.txt").readlines() ))

mx = 0
my = 0
for l in input:
    (x,y) = map(int, l.split(','))
    if x > mx:
        mx = x
    if y > my:
        my = y

mx += 1
my += 1
data = np.full((my, mx), np.inf)
data_name = np.zeros((my,mx), dtype=int)

i = 1
for l in input:
    (x,y) = map(int, l.split(','))
  
    #data[y][x] = 0
    data_name[y][x] = i 

    for xx in range(0,mx):
        for yy in range(0,my):
            d = dist(x,y,xx,yy)
            if  d < data[yy][xx]:
                data_name[yy][xx] = i
                data[yy][xx] = d
            elif d == data[yy][xx]:
                data_name[yy][xx] = -1

    
    i +=1

total = {}
for j in data_name:
    for k in j:
        if k in total:
            total[k] += 1
        else:
            total[k] = 1

for j in data_name[0]:
    total[j] = -1

for j in data_name[-1]:
    total[j] = -1

for j in data_name:
    total[ j[0] ] = -1
    total[ j[-1] ] = -1

m = 0
for i in total:
    if total[i] > m:
        m = total[i]
print(total)
print(m)

#print(data)
print(data_name)
#print (np.bincount(data_name))