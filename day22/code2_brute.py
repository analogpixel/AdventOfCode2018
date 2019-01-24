#!/usr/bin/env python

import numpy as np
import sys
import math

sys.setrecursionlimit(225000)

import gc
gc.disable()


depth=7863
elf_x=14
elf_y=760

#depth=510
#elf_x=10
#elf_y=10

geo_index = [[0 for i in range(elf_x+6)] for j in range(elf_y+6)]
ero_index = [[0 for i in range(elf_x+6)] for j in range(elf_y+6)]

t = ['.', '=', '|']

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

# distance * 7 would be if you switched tool each time
# so lets try dist * 5?
mmin=int(elf_x + elf_y * 5) 
max_time_g=int(elf_x + elf_y * 5) 
mmin=3000
max_moves = elf_x + elf_y + 10

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
    global mmin
    maxtime = max_time_g

    # don't take too long
    if minutes > mmin or conswitch > 300:
        return maxtime
    
    if x == elf_x and y == elf_y:
        # if you don't have the torch, you have to switch to it to find him
        if not eq == 1:
            minutes += 7
        if minutes < mmin:
            mmin = minutes
            print("---")
            print(already)
            print("Got there in", minutes, " With:", conswitch , " switches")
            print("---")
        return minutes

    
    # don't let the path get too long
    if len(already) > max_moves:
        return maxtime

    # now try every direction with all types of equipment
    # and return the least score you get back
    scores = []
    for dir in [ (0,1), (1,0) , (0,-1), (-1,0) ]:
        # don't backtrack?
        if (x+dir[0], y+dir[1]) in already:
            continue

        # don't move backwards unless we have passed the elf?
        if y < elf_y and dir == (0,-1):
            continue
        if x < elf_x and dir == (-1,0):
            continue

        # don't leave the map    
        if x + dir[0] > elf_x+5:
            continue
        if x + dir[0] < 0:
            continue
        if y + dir[1] > elf_y + 5:
            continue
        if y + dir[1] < 0:
            continue
        
        a = ero_index[y][x]
        b = ero_index[y+dir[1]][x+dir[0]]
        # 0: rock : climbing gear(2) or torch(1)
        # 1: wet : climbing gear(2) or neither(0)
        # 2: narrow : torch(1) or neither(0)
        #
        # 0: neither
        # 1: torch
        # 2: climbing gear
        if a == 0 and b==0:
            scores.append(  solve(eq, x+dir[0], y+dir[1], minutes + 1, already + [(x+dir[0], y+dir[1])], conswitch )  )
        elif a == 0 and b == 1: 
            if eq == 2:
                scores.append(  solve(2, x+dir[0], y+dir[1], minutes + 1, already + [(x+dir[0], y+dir[1])], conswitch )  )
            else:
                scores.append(  solve(2, x+dir[0], y+dir[1], minutes + 8, already + [(x+dir[0], y+dir[1])], conswitch +1 )  )
        elif a == 0 and b == 2:
            if eq == 1:
                scores.append(  solve(1, x+dir[0], y+dir[1], minutes + 1, already + [(x+dir[0], y+dir[1])], conswitch )  )
            else:
                scores.append(  solve(1, x+dir[0], y+dir[1], minutes + 8, already + [(x+dir[0], y+dir[1])], conswitch +1 )  )
        elif a == 1 and b == 0:
            if eq == 2:
                scores.append(  solve(2, x+dir[0], y+dir[1], minutes + 1, already + [(x+dir[0], y+dir[1])], conswitch )  )
            else:
                scores.append(  solve(2, x+dir[0], y+dir[1], minutes + 8, already + [(x+dir[0], y+dir[1])], conswitch +1 )  )
        elif a == 1 and b == 1:
            scores.append(  solve(eq, x+dir[0], y+dir[1], minutes + 1, already + [(x+dir[0], y+dir[1])], conswitch  )  )
        elif a == 1 and b == 2:
            if eq == 0:
                scores.append(  solve(0, x+dir[0], y+dir[1], minutes + 1, already + [(x+dir[0], y+dir[1])], conswitch )  )
            else:
                scores.append(  solve(0, x+dir[0], y+dir[1], minutes + 8, already + [(x+dir[0], y+dir[1])], conswitch +1 )  )
        elif a == 2 and b == 0:
            if eq == 1:
                scores.append(  solve(1, x+dir[0], y+dir[1], minutes + 1, already + [(x+dir[0], y+dir[1])], conswitch )  )
            else:
                scores.append(  solve(1, x+dir[0], y+dir[1], minutes + 8, already + [(x+dir[0], y+dir[1])], conswitch +1 )  )
        elif a == 2 and b == 1:
            if eq == 0:
                scores.append(  solve(0, x+dir[0], y+dir[1], minutes + 1, already + [(x+dir[0], y+dir[1])], conswitch  )  )
            else:
                scores.append(  solve(0, x+dir[0], y+dir[1], minutes + 8, already + [(x+dir[0], y+dir[1])], conswitch +1 )  )
        elif a == 2 and b == 2:
            scores.append(  solve(eq, x+dir[0], y+dir[1], minutes + 1, already + [(x+dir[0], y+dir[1])], conswitch  )  )    
        

    if len(scores) == 0:
        return maxtime
    else:
        return min(scores)


print(  solve(1, 0,0, 0, [(0,0)],0)) 
