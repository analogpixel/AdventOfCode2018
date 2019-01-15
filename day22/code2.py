#!/usr/bin/env python

# pip install Dijkstar

import numpy as np
import sys
from dijkstar import Graph, find_path

sys.setrecursionlimit(225000)

depth=7863
elf_x=14
elf_y=760

#depth=510
#elf_x=10
#elf_y=10

geo_index = np.full((elf_y+6, elf_x+6), 0)
ero_index = np.full((elf_y+6, elf_x+6), 0)

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

        ero_index[y][x] = ((geo_index[y][x] + depth) % 20183) 

for x in range(0, elf_x+6):
    for y in range(0, elf_y+6):
        ero_index[y][x] = ero_index[y][x] % 3

def costFunction(current_node, neightbor_node, edge, prev_edge):
    if edge['cost']:
        return 1
    else:
        return 8

graph = Graph()
for x in range(0,elf_x+6):
    for y in range(0, elf_y+6):
        for dir in [ (0,1), (1,0) , (0,-1), (-1,0) ]:
            if x + dir[0] < 0:
                continue
            if x + dir[0] > elf_x:
                continue
            if y + dir[1] < 0:
                continue
            if y + dir[1] > elf_y:
                continue
            graph.add_edge( str(x) + "_" +  str(y),   str(x+dir[0]) + "_"  + str( y+dir[1]) , {'cost':  ero_index[y][x] == ero_index[y+dir[1]][x+dir[0]] } )


f = find_path(graph, '0_0' , d='14_760', cost_func=costFunction) 
print(f.nodes, len(f.nodes), f.total_cost- len(f.nodes) -3)

