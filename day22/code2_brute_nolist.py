#!/usr/bin/env python

import numpy as np
import sys
import math
from pairing import pair

# 2797 is too high
# 1809 is too high

sys.setrecursionlimit(225000)

import gc
gc.disable()


depth=7863
elf_x=14
elf_y=760

depth=510
elf_x=10
elf_y=10

geo_index = [[0 for i in range(elf_x+6)] for j in range(elf_y+6)]
ero_index = [[0 for i in range(elf_x+6)] for j in range(elf_y+6)]

t = ['.', '=', '|']


# trying to speed up dict key creation
sc = {}
for y in range(0, elf_y+16):
    a = {}
    for x in range(0, elf_x+16):
        a[x] = pair(x,y)
    sc[y] = a


for x in range(0, elf_x+6):
    for y in range(0, elf_y+6):
        if (x==elf_x) and (y==elf_y):
            geo_index[y][x] = 0
        elif x==0 and y==0:
            geo_index[y][x] == 0
        elif y == 0:
            geo_index[y][x] = x * 16807
        elif x == 0:
            geo_index[y][x] = y * 48271
        else:
            geo_index[y][x] = ero_index[y][x-1] * ero_index[y-1][x]

        ero_index[y][x] =  ((geo_index[y][x] + depth) % 20183) 
    
for x in range(0, elf_x+6):
    for y in range(0, elf_y+6):
        ero_index[y][x] = ero_index[y][x] % 3

for e in ero_index:
    print("".join(map(lambda x: t[x%3], e)))

max_switches = 280
max_moves = elf_x + elf_y + 10
mmin = max_switches * 8 + ((elf_x + elf_y) - max_switches)
max_time_g=int(elf_x + elf_y * 8)

print("max_Switch set to: {}  mmin set to: {}".format(max_switches, mmin))

# eq: 0 : neither  1: torch  2: climbing gear
# x,y positio to move to
# px,pt: prevous x,y so you don't back track
# minutes: how long you've taken
#
# 0: rock : climbing gear(2) or torch(1)
# 1: wet : climbing gear(2) or neither(0)
# 2: narrow : torch(1) or neither(0)
#
def solve(eq,x,y,minutes,already,conswitch):
    global mmin, max_switches
    maxtime = max_time_g

    # don't take too long
    #if minutes > mmin or conswitch > 300 or len(already) > max_moves:
    if minutes > mmin or conswitch > max_switches or len(already) > max_moves:
        return maxtime
    
    if x == elf_x and y == elf_y:
        # if you don't have the torch, you have to switch to it to find him
        if not eq == 1:
            minutes += 7
        if minutes < mmin:
            mmin = minutes
            max_switches = conswitch
            print("---")
            #print(already)
            print("Got there in", minutes, " With:", conswitch , " switches")
            print("---")
        return minutes

    # if you are in an area with the wrong equipment
    # just cancel out
    if ero_index[y][x]  == 0 and eq not in [2,1]:
        return maxtime
    if ero_index[y][x]  == 1 and eq not in [2,0]:
        return maxtime
    if ero_index[y][x]  == 2 and eq not in [1,0]:
        return maxtime
    

    # now try every direction with all types of equipment
    # and return the least score you get back
    scores = []
    for dir in [ (0,1), (1,0) , (0,-1), (-1,0) ]:

        # don't move backwards unless we have passed the elf?
        if y < elf_y and dir == (0,-1):
            continue
        if x < elf_x and dir == (-1,0):
            continue

        new_x = x+dir[0]
        new_y = y+dir[1]
        # don't leave the map    
        if new_x > elf_x+5:
            continue
        elif new_x < 0:
            continue
        elif new_y > elf_y + 5:
            continue
        elif new_y < 0:
            continue
        
        xykey = sc[y+dir[1]][x+dir[0]]
        
        # don't backtrack?
        if xykey in already:
            continue
        
        if ero_index[y][x]  == 0:
            valid_eq = [2,1]
        elif ero_index[y][x] == 1:
            valid_eq = [2,0]
        elif ero_index[y][x]  == 2:
            valid_eq = [1,0]
    
        i = 0
        scores = [6000,6000,6000]
        for new_eq in valid_eq:
            if new_eq == eq:
                t = 1
                scores[i] = solve(new_eq, new_x, new_y, minutes + t, already + [xykey], conswitch )
            else:
                t = 8 # 7 to change 1 to move
                scores[i] = solve(new_eq, new_x, new_y, minutes + t, already + [xykey], conswitch+1 )
            i +=1

    if len(scores) == 0:
        return maxtime
    else:
        return min(scores)


print(  solve(1, 0,0, 0, [],0)) 
