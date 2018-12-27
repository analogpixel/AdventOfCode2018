#!/usr/bin/env python

import numpy as np

depth=7863
elf_x=14
elf_y=760

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

"""
for e in ero_index:
    print("".join(map(lambda x: t[x%3], e)))
"""

t = 0
for x in range(0, elf_x+1):
    for y in range(0, elf_y+1):
        t += ero_index[y][x] % 3
    
print(t)