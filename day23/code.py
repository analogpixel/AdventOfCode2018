#!/usr/bin/env python

import re

input_file = "input.txt"

input = list(map( lambda x: x.strip(), open(input_file).readlines() ))

max_size = 0
max_pos=(0,0,0)
for i in range(0, len(input)):
    m = re.match( r'pos=<(.*)>, r=(.*)' , input[i])
    size = int(m.group(2))
    if size > max_size:
        max_size = size
        max_pos = list(map(int, m.group(1).split(',')))

count = 0
x = []
y = []
z = []
for i in range(0, len(input)):
    m = re.match( r'pos=<(.*)>, r=(.*)' , input[i])
    pos = list(map(int, m.group(1).split(',')))
    size = int(m.group(2))

    dist = abs(max_pos[0] - pos[0]) + abs(max_pos[1] - pos[1]) + abs( max_pos[2] - pos[2])

    if dist <= max_size:
        print(pos)
        count +=1 

    x.append(pos[0])
    y.append(pos[1])
    z.append(pos[2])


print("Count:{} max_x:{} min_x:{} max_y:{} min_y:{} max_z:{} min_z{}".format(count, max(x), min(x), max(y), min(y), max(z), min(z)))

