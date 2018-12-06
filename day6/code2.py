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

count=0
regionSize = 10000
# loop through all the points
for ix in range(0,mx):
    for jy in range(0,my):
        dTotal = 0
        for l in input:
            # get a distance to each point from this point
            (x,y) = map(int, l.split(','))
            dTotal += dist(x,y, ix,jy)
        
        data[jy][ix] = dTotal
        if dTotal < regionSize:
            count +=1

print(data)
print(count)