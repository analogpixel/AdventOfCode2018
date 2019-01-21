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
bots = []
for i in range(0, len(input)):
    m = re.match( r'pos=<(.*)>, r=(.*)' , input[i])
    pos = list(map(int, m.group(1).split(',')))
    size = int(m.group(2))

    bots.append( [pos, size] )
    dist = abs(max_pos[0] - pos[0]) + abs(max_pos[1] - pos[1]) + abs( max_pos[2] - pos[2])

    if dist <= max_size:
        #print(pos)
        count +=1 

    x.append(pos[0])
    y.append(pos[1])
    z.append(pos[2])

max_in_range = 0
max_scores = []
for xx in range(min(x), max(x)+1):
    for yy in range(min(y), max(y)+1):
        for zz in range(min(z), max(z)+1):
            in_range=0
            for b in bots:
                d = abs(b[0][0] - xx) + abs(b[0][1] - yy) +abs(b[0][2] - zz)
                if d <= b[1]:
                    in_range +=1
            if max_in_range <= in_range:
                if max_in_range == in_range:
                    max_scores.append([xx,yy,zz])
                else:
                    max_scores = [[xx,yy,zz]]
                    max_in_range = in_range

mdist = 9999
mdist_loc = []
for score in max_scores:
    print
    t = abs(score[0]) + abs(score[1]) + abs(score[2])
    if t< mdist:
        mdist = t
        mdist_loc = [score[0], score[1], score[2]]

print(mdist, mdist_loc)
