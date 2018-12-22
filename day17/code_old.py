#!/usr/bin/env python

# pip install pypng


import numpy as np 
import png

input_file = "test_input.txt"
w=2000
h=2000

clay=255
water=50
standing_water=90
hole=25
sand=0

## Build the initil map
mymap = np.full((w,h), sand)
mymap[0][500] = hole
input = list(map( lambda x: x.strip(), open(input_file).readlines() ))
for line in input:    
    (p1,p2) = line.split(',')
    p1 = int(p1.split('=')[1])
    p2 = p2.split('=')[1]
    (p2_1, p2_2) = map(int, p2.split('..'))


    if line[0] == 'x':
        for y in range(p2_1, p2_2+1):
            mymap[y][p1] = clay
    elif line[0] == 'y':
        for x in range(p2_1, p2_2+1):
            mymap[p1][x] = clay



for zzz in range(0,5):
    px = 500
    py = 0

    # fall until something is hit
    py += 1
    while (mymap[py][px] != clay) and (mymap[py][px] != standing_water):
        mymap[py][px] = water
        py +=  1

    py -= 1
    # look side to side to see if we are enclosed
    right_enclosed = False
    left_enclosed = False
    for i in range(px,-1, -1):
        # if no clay under it, then it's not enclosed
        if  mymap[py+1][i] not in [clay, standing_water]:
            break
        if mymap[py][i] == clay:
            left_enclosed = i+1
            break
        
    for i in range(px, w):
        # if no clay under it, then it's not enclosed
        if  mymap[py+1][i] not in [clay, standing_water]:
            break
        if mymap[py][i] == clay and mymap[py+1][i] == clay:
            right_enclosed = i
            break
    
    if right_enclosed and left_enclosed:
        for i in range(left_enclosed, right_enclosed):
            mymap[py][i] = standing_water
    

    # if not enclosed then flow out the sides that not enclosed

    # if enclosed then fill the layer with standing water


    #break
    




png.from_array(mymap[0:40, 450:600],  'L;8').save("map.png")
